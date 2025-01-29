#!/usr/bin/env python3

import sys
import json
import glob
import os
from pathlib import Path

# Import functions from other scripts
from blossom_upload import calculate_sha256, test_server
from get_path_details import extract_arch_info
from feed_repo_data import concatenate_repos

def run_blossom_upload(file_path):
    """Run blossom upload functionality directly"""
    try:
        secrets_path = os.path.join(os.path.dirname(__file__), 'blossom_secrets.json')
        print("secrets path: ", str(secrets_path))
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
            
            # Map module name to directory name
            module_dir_map = {
                "golang": "lang",
                "golang-src": "lang",
                "golang-doc": "lang",
                "tollgate-module-valve-go": "valve",
                "tollgate-module-merchant-go": "merchant",
                "tollgate-module-relay-go": "tollgate-module-relay-go",
                "tollgate-module-whoami-go": "whoami",
                "tollgate-module-crowsnest-go": "crowsnest",
            }
            
            module_dir = module_dir_map.get(module_name, module_name)

            # Construct the Makefile path
            makefile_path = os.path.join(sdk_path, "feeds", "custom", module_dir, "Makefile")
            print(f"makefile_path: {makefile_path}")

            
            branch_name = "unknown"
            commit_hash = "unknown"
            
            if os.path.exists(makefile_path):
                with open(makefile_path, 'r') as f:
                    for line in f:
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
    event += f"#openwrt #{full_arch} #{target_platform}"
    
    return event

def write_note(data, note_path):
    """Write data to note.md"""
    with open(note_path, 'w') as f:
        f.write(data)

def main():
    if len(sys.argv) != 4:
        error = {
            "error": f"Usage: {sys.argv[0]} <path_to_packages_directory> <path_to_feeds.conf> <sdk_path>"
        }
        print(json.dumps(error, indent=2))
        sys.exit(1)

    package_dir = sys.argv[1]
    feeds_conf = sys.argv[2]
    sdk_path = sys.argv[3]

    if not os.path.isdir(package_dir):
        print(json.dumps({"error": f"Directory not found: {package_dir}"}, indent=2))
        sys.exit(1)

    if not os.path.isfile(feeds_conf):
        print(json.dumps({"error": f"File not found: {feeds_conf}"}, indent=2))
        sys.exit(1)

    if not os.path.isdir(sdk_path):
        print(json.dumps({"error": f"SDK directory not found: {sdk_path}"}, indent=2))
        sys.exit(1)

    # Print final aggregated JSON
    nostr_event=create_nostr_event(package_dir, feeds_conf, sdk_path)
    
    # Write to note.md
    note_path = Path('note.md')
    write_note(nostr_event, note_path)
    print(nostr_event)


if __name__ == "__main__":
    main()
