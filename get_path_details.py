import os
import re
import sys
import json

def extract_arch_info(path):
    # If the path is a file, get its directory
    if os.path.isfile(path):
        path = os.path.dirname(path)
    
    # Split the path into components
    path_parts = path.split(os.sep)
    
    # Find the components we're interested in by looking for the 'packages' directory
    try:
        packages_index = path_parts.index('packages')
        if packages_index + 1 < len(path_parts):
            # Get architecture info (e.g. 'aarch64_cortex-a53' or 'mips_24kc')
            arch = path_parts[packages_index + 1]
            
            # Extract base architecture and variant
            match = re.match(r'([^_]+)_(.+)', arch)
            if match:
                base_arch = match.group(1)    # e.g. 'aarch64' or 'mips'
                arch_variant = match.group(2)  # e.g. 'cortex-a53' or '24kc'
            else:
                base_arch = arch
                arch_variant = ''
                
            # Get SDK name and extract target platform
            sdk_name = next((part for part in path_parts if part.startswith('openwrt-sdk-')), '')
            
            # Extract target platform (e.g. 'ath79-generic' or 'mediatek-filogic')
            platform_match = re.search(r'openwrt-sdk-[\d\.]+-([^_]+)', sdk_name)
            if platform_match:
                target_platform = platform_match.group(1)
                # Split platform into type and variant
                platform_parts = target_platform.split('-')
                platform_type = platform_parts[0]      # e.g. 'ath79' or 'mediatek'
                platform_variant = platform_parts[1] if len(platform_parts) > 1 else ''  # e.g. 'generic' or 'filogic'
            else:
                target_platform = ''
                platform_type = ''
                platform_variant = ''
                
            return {
                'full_arch': arch,
                'base_arch': base_arch,
                'arch_variant': arch_variant,
                'sdk_name': sdk_name,
                'target_platform': target_platform,
                'platform_type': platform_type,
                'platform_variant': platform_variant
            }
    except ValueError:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 get_path_details.py <path>")
        sys.exit(1)
        
    path = sys.argv[1]
    info = extract_arch_info(path)
    if info:
        print(json.dumps(info, indent=2))
    else:
        print(json.dumps({"error": "Could not extract information from path"}, indent=2))
