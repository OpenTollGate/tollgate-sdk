#!/usr/bin/env python3

import sys
import json
import subprocess
import hashlib
import os
import tempfile

def calculate_sha256(file_path):
    """Calculate SHA256 hash of a file"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def test_server(server, input_file, original_hash, secret_key):
    """Test upload and download for a single server"""
    # Set environment variable
    env = os.environ.copy()
    env['NOSTR_SECRET_KEY'] = secret_key
    
    # Upload file
    upload_proc = subprocess.run(
        ['blossom', 'upload', '-server', server, input_file],
        capture_output=True,
        text=True,
        env=env
    )
    
    if upload_proc.returncode != 0:
        return False
        
    # Get hash from upload response
    try:
        upload_hash = json.loads(upload_proc.stdout)['sha256']
    except (json.JSONDecodeError, KeyError):
        return False
    
    # Download to temp file
    with tempfile.NamedTemporaryFile() as tmp_file:
        download_proc = subprocess.run(
            ['blossom', 'download', '-server', server, upload_hash],
            stdout=tmp_file,
            env=env
        )
        
        if download_proc.returncode != 0:
            return False
            
        # Verify hash
        downloaded_hash = calculate_sha256(tmp_file.name)
        
        return original_hash == downloaded_hash

def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": f"Usage: {sys.argv[0]} <file_to_upload>"}))
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
        print(json.dumps({"error": f"Error: File '{input_file}' does not exist"}))
        sys.exit(1)

    # Read secrets
    try:
        secrets_path = os.path.join(os.path.dirname(__file__), 'blossom_secrets.json')
        print("secrets path: ", str(secrets_path))
        with open(secrets_path) as f:
            secrets = json.load(f)
            secret_key = secrets['secret_key']
            servers = secrets['servers']
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(json.dumps({"error": f"Error reading secrets file: {str(e)}"}))
        sys.exit(1)

    # Calculate original file hash
    original_hash = calculate_sha256(input_file)
    
    # Test each server
    successful_servers = []
    for server in servers:
        if test_server(server, input_file, original_hash, secret_key):
            successful_servers.append(server)

    # Create result JSON
    result = {
        original_hash: successful_servers
    }
    
    # Output JSON to stdout
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
