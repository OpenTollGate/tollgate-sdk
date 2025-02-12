#!/usr/bin/env python3

import sys
import json
import re
import tempfile
import os
import subprocess
from pathlib import Path

def get_current_repo_info():
    """Get information about the current repository"""
    # Get the directory where the script is located
    script_dir = Path(__file__).parent.absolute()
    
    # Get the directory name
    dir_name = script_dir.name
    
    # Get git information
    result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                            cwd=script_dir,
                            stdout=subprocess.PIPE,
                            text=True)
    current_branch = result.stdout.strip()
    
    result = subprocess.run(['git', 'rev-parse', 'HEAD'],
                            cwd=script_dir,
                            stdout=subprocess.PIPE,
                            text=True)
    commit_hash = result.stdout.strip()
    
    # Create path with replaced username
    sanitized_path = str(script_dir).replace(os.path.expanduser('~'), '[c03rad0r]')
    
    return {
        commit_hash: {
            "directory": dir_name,
            "branch": current_branch
        }
    }

def get_remote_hash(url, ref):
    """Get commit hash for a remote reference without cloning"""
    result = subprocess.run(['git', 'ls-remote', url, ref],
                          stdout=subprocess.PIPE,
                          text=True)
    if result.stdout:
        # First word of output is the commit hash
        return result.stdout.split()[0]
    return None

def parse_feeds_conf(feeds_conf_path):
    """Parse feeds.conf and return repository information"""
    repos = {}
    
    # Regular expression for matching feed lines
    feed_pattern = re.compile(r'src-git(?:-full)?\s+(\S+)\s+(https://[^;\s]+)(?:\^([a-f0-9]+)|;([^;\s]+))?')
    
    with open(feeds_conf_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                match = feed_pattern.match(line)
                if match:
                    feed_name, url, commit_hash, branch = match.groups()
                    
                    if feed_name == "custom":
                        # For custom repo, clone and get hash
                        commit_hash = get_remote_hash(url, branch)
                        repos[commit_hash] = {
                            "directory": feed_name,
                            "branch": branch if branch else ""
                        }
                    elif commit_hash:
                        # Direct commit hash in URL
                        repos[commit_hash] = {
                            "directory": feed_name,
                            "branch": commit_hash
                        }
                    elif branch:
                        try:
                            commit_hash = get_remote_hash(url, branch)
                            if commit_hash:
                                repos[commit_hash] = {
                                    "directory": feed_name,
                                    "branch": branch
                                }
                            else:
                                # Fallback to branch name if can't get hash
                                repos[branch] = {
                                    "directory": feed_name,
                                    "branch": branch
                                }
                        except Exception as e:
                            print(f"Error getting remote hash: {e}")
                            repos[branch] = {
                                "directory": feed_name,
                                "branch": branch
                            }
    return repos

def write_git_info(data, git_info_path):
    """Write data to git_info.json"""
    with open(git_info_path, 'w') as f:
        json.dump(data, f, indent=2)

def concatenate_repos(feeds_conf_path):
    # Get current repository information
    repos = get_current_repo_info()
    
    # Add feed repository information
    repos.update(parse_feeds_conf(feeds_conf_path))

    return json.dumps(repos, indent=2)
    
def main():
    if len(sys.argv) != 2:
        error_msg = {"error": f"Usage: {sys.argv[0]} <path_to_feeds.conf>"}
        print(json.dumps(error_msg, indent=2))
        sys.exit(1)
        
    feeds_conf_path = Path(sys.argv[1])
    if not feeds_conf_path.is_file():
        error_msg = {"error": f"Error: {feeds_conf_path} does not exist"}
        print(json.dumps(error_msg, indent=2))
        sys.exit(1)
        
    
    # Write to git_info.json
    # git_info_path = Path('git_info.json')
    # write_git_info(concatenate_repos(feeds_conf_path), git_info_path)
    
    # Print JSON to stdout
    # print(json.dumps(repos, indent=2))
    print(concatenate_repos(feeds_conf_path))

if __name__ == "__main__":
    main()
