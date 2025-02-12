#!/bin/bash

# Require root privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run with sudo"
    exit 1
fi

# Preserve the original user's GOPATH
ORIGINAL_USER=$(logname)
export GOPATH="/home/$ORIGINAL_USER/go"
export PATH="$PATH:/usr/local/go/bin:$GOPATH/bin"

# Create a directory for the project
echo "Creating directory for Blossom..."
mkdir -p /opt/blossom
cd /opt/blossom

# Clone the repository if not exists
if [ ! -d "blossom" ]; then
    git clone https://git.fiatjaf.com/blossom .
fi

# Download Go dependencies
echo "Downloading Go dependencies..."
go mod download

# Build the project
echo "Building Blossom..."
go build -o blossom .

# Make the binary executable and move to system-wide location
echo "Installing Blossom system-wide..."
chmod +x blossom
cp blossom /usr/local/bin/

# Print success message
echo "Blossom has been successfully installed!"
echo "The blossom binary is now available system-wide in /usr/local/bin"
