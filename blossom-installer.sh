#!/bin/bash

# Check if Go is installed
if ! command -v go &> /dev/null; then
    echo "Error: Go is not installed. Please install Go first."
    exit 1
fi

# Create a directory for the project
echo "Creating directory for Blossom..."
mkdir -p ~/blossom
cd ~/blossom

# Clone the repository
# echo "Cloning Blossom repository..."
# git clone https://git.fiatjaf.com/blossom

# Download Go dependencies
echo "Downloading Go dependencies..."
go mod download

# Build the project
echo "Building Blossom..."
go build -o blossom .

# Make the binary executable
chmod +x blossom

# Add to PATH (optional)
echo "Adding Blossom to PATH..."
mkdir -p ~/bin
cp blossom ~/bin/

# Update PATH in shell configuration if needed
if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
    echo "Please restart your shell or run 'source ~/.bashrc' to update PATH"
fi

# Print success message
echo "Blossom has been successfully installed!"
echo "You can now use 'blossom' from anywhere in your terminal"
echo "Example usage:"
echo "blossom upload -server <server_url> -file <file_path> -privkey <private_key>"
