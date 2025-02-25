#!/usr/bin/env python3

import sys
import json
import glob
import os
from pathlib import Path
from nostr.event import Event
from nostr.key import PrivateKey
from nostr.relay_manager import RelayManager
from blossom_upload import calculate_sha256, test_server
from get_path_details import extract_arch_info
from feed_repo_data import concatenate_repos
import time
import ssl

print("=== Debug Information ===")
print(f"Script starting at: {os.path.abspath(__file__)}")
print(f"Current working directory: {os.getcwd()}")
print(f"PYTHONPATH: {os.environ.get('PYTHONPATH', 'Not set')}")
print(f"Python path: {sys.path}")
print("=== End Debug Info ===")

SECRETS_FILE="blossom_secrets.json"

def run_blossom_upload(file_path):
    """Run blossom upload functionality directly"""
    try:
        secrets_path = os.path.join(os.path.dirname(__file__), SECRETS_FILE)
        with open(secrets_path) as f:
            secrets = json.load(f)
            secret_key = secrets['secret_key']
            servers = secrets['servers']
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        return {"error": f"Error reading secrets file: {str(e)}"}

    # Calculate original file hash
    original_hash = calculate_sha256(file_path)
    
    # Test each server
    successful_servers = []
    for server in servers:
        if test_server(server, file_path, original_hash, secret_key):
            successful_servers.append(server)

    # Create result dictionary
    return {
        original_hash: successful_servers
    }

def aggregate(package_dir, feeds_conf, sdk_path):
    # Initialize result dictionary
    result = {
        "binaries": {},
        "target_info": {},
        "feed_info": {}
    }

    # Get path details
    path_details = extract_arch_info(package_dir)
    if path_details:
        result["target_info"] = {
            "target_platform": path_details["target_platform"],
            "full_arch": path_details["full_arch"]
        }
    else:
        return json.dumps({"error": "Could not extract path details"}, indent=2)

    # Get feed data
    try:
        feed_data = json.loads(concatenate_repos(feeds_conf))
        result["feed_info"] = feed_data
    except Exception as e:
        return json.dumps({"error": f"Error getting feed data: {str(e)}"}, indent=2)

    # Process each .ipk file in the directory
    ipk_files = glob.glob(os.path.join(package_dir, "*.ipk"))
    print(f"Found {len(ipk_files)} .ipk files to process")

    for file_path in ipk_files:
        if os.path.isfile(file_path):
            print(f"\nUploading {os.path.basename(file_path)}...")

            # Extract module name from filename
            filename = os.path.basename(file_path)
            module_name = filename.split("_")[0]
            
            # TODO: ensure that this map isn't required in future
            # Map module name to directory name
            module_dir_map = {
                "golang": "lang",
                "golang-src": "lang",
                "golang-doc": "lang",
                "tollgate-module-valve-go": "tollgate-module-valve-go",
                "tollgate-module-merchant-go": "tollgate-module-merchant-go",
                "tollgate-module-relay-go": "tollgate-module-relay-go",
                "tollgate-module-updater-go": "tollgate-module-updater-go",
                "tollgate-module-whoami-go": "tollgate-module-whoami-go",
                "tollgate-module-crowsnest-go": "tollgate-module-crowsnest-go",
            }
            
            # module_dir = module_dir_map.get(module_name, module_name)
            module_dir = module_name

            # Construct the Makefile path
            makefile_path = os.path.join(sdk_path, "feeds", "custom", module_dir, "Makefile")
            print(f"makefile_path: {makefile_path}")

            
            branch_name = "unknown"
            commit_hash = "unknown"
            
            if os.path.exists(makefile_path):
                with open(makefile_path, 'r') as f:
                    for line in f:
                        print("line: " + str(line))
                        if line.startswith("PKG_SOURCE_VERSION:="):
                            branch_name = line.split(":=")[1].strip()
                            print(f"branch_name after reading: {branch_name}")
                        if line.startswith("PKG_SOURCE_COMMIT:="):
                            commit_hash = line.split(":=")[1].strip()

            blossom_result = run_blossom_upload(file_path)
            
            # Check if there was an error
            if "error" in blossom_result:
                print(f"Error uploading {os.path.basename(file_path)}: {blossom_result['error']}")
                continue
                
            # Store results indexed by filename
            filename = os.path.basename(file_path)
            result["binaries"][filename] = {
                "file_hash": list(blossom_result.keys())[0],
                "servers": list(blossom_result.values())[0],
                "branch": branch_name,
                "commit": commit_hash
            }
            print(f"Successfully uploaded {filename}")

    return json.dumps(result, indent=2)

def create_nostr_event(package_dir, feeds_conf, sdk_path):
    # Get the JSON result
    json_result = aggregate(package_dir, feeds_conf, sdk_path)
    
    # Parse the JSON to extract target info for hashtags
    result_dict = json.loads(json_result)
    
    # Get target info for hashtags
    target_info = result_dict.get("target_info", {})
    full_arch = target_info.get("full_arch", "unknown")
    target_platform = target_info.get("target_platform", "unknown")
    
    # Create the event string
    event = f"```\n{json_result}\n```\n\n"
    event += f"#OpenWRT-image #{full_arch} #{target_platform}"
    
    return event

def write_note(data, note_path):
    """Write data to note.md"""
    with open(note_path, 'w') as f:
        f.write(data)

def publish_note(data):
    """Publish note to nostr relays with resilient handling"""
    try:
        secrets_path = os.path.join(os.path.dirname(__file__), SECRETS_FILE)
        with open(secrets_path) as f:
            secrets = json.load(f)
            secret_key_hex = secrets['secret_key_hex']
            relays = secrets['relays']

        private_key = PrivateKey(bytes.fromhex(secret_key_hex))
        event = Event(content=data, public_key=private_key.public_key.hex())
        private_key.sign_event(event)

        successful_publish = False
        
        # Try each relay individually
        for relay_url in relays:
            try:
                # Initialize relay manager with single relay
                relay_manager = RelayManager()
                relay_manager.add_relay(relay_url)
                
                relay_manager.open_connections({"cert_reqs": ssl.CERT_NONE})
                time.sleep(1.25)  # give the relay time to connect
                
                # Attempt to publish
                relay_manager.publish_event(event)
                time.sleep(1)  # wait for publishing
                
                successful_publish = True
                print(f"Successfully published to {relay_url}")
                
            except Exception as e:
                print(f"Failed to publish to {relay_url}: {str(e)}")
            
            finally:
                try:
                    relay_manager.close_connections()
                except:
                    pass
            
            # Break if we've had a successful publish
            if successful_publish:
                break
        
        if not successful_publish:
            print("Warning: Failed to publish to any relay")
            # Optionally, you could raise an exception here if you want to fail the script
            # raise Exception("Failed to publish to any relay")
        
        return successful_publish

    except Exception as e:
        print(f"Error in publish_note: {str(e)}")
        return False
 
def main():
    if len(sys.argv) != 4:
        error = {
            "error": f"Usage: <path_to_packages_directory> <path_to_feeds.conf> <sdk_path>"
        }
        print(json.dumps(error, indent=2), file=sys.stderr)
        sys.exit(1)

    package_dir = sys.argv[1]
    feeds_conf = sys.argv[2]
    sdk_path = sys.argv[3]

    if not os.path.isdir(package_dir):
        print(json.dumps({"error": f"Directory not found: {package_dir}"}, indent=2), file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(feeds_conf):
        print(json.dumps({"error": f"File not found: {feeds_conf}"}, indent=2), file=sys.stderr)
        sys.exit(1)

    if not os.path.isdir(sdk_path):
        print(json.dumps({"error": f"SDK directory not found: {sdk_path}"}, indent=2))
        sys.exit(1)

    # Print final aggregated JSON
    nostr_event = create_nostr_event(package_dir, feeds_conf, sdk_path)
    json_result = aggregate(package_dir, feeds_conf, sdk_path)

    # Write to note.md
    note_path = Path('note.md')
    
    # Attempt to publish, but continue even if it fails
    publish_success = publish_note(nostr_event)
    if not publish_success:
        print("Warning: Note publication failed, but continuing with other operations")
    
    print(json_result)


if __name__ == "__main__":
    main()
