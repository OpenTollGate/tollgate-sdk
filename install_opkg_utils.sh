#!/bin/bash
set -e

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install required dependencies
install_dependencies() {
    echo "Installing build dependencies..."
    sudo apt-get update
    sudo apt-get install -y build-essential autoconf automake libtool pkg-config git
}

# Function to build and install opkg-utils
install_opkg_utils() {
    echo "Checking if opkg-make-index exists..."
    if command_exists opkg-make-index; then
        echo "opkg-make-index is already installed."
    else
        echo "opkg-make-index not found, proceeding with manual installation..."

        # Create temporary directory for building opkg-utils
        TEMP_DIR=$(mktemp -d)
        echo "Created temporary directory: $TEMP_DIR"
        
        # Clone opkg repository and build opkg-utils
        git clone https://git.openwrt.org/project/opkg-lede.git "$TEMP_DIR/opkg-lede"
        cd "$TEMP_DIR/opkg-lede"
        git submodule update --init
        mkdir -p build
        cd build
        cmake ..
        make

        # Install opkg-make-index
        sudo cp utils/opkg-make-index /usr/local/bin/
        echo "opkg-make-index installed successfully."

        # Cleanup
        cd ~
        rm -rf "$TEMP_DIR"
        echo "Cleaned up temporary files."
    fi
}

# Main logic
install_dependencies
install_opkg_utils

echo "Installation and cleanup completed successfully."
