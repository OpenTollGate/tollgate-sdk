#!/bin/bash
set -e

# Require root privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run with sudo"
    exit 1
fi

# Install system dependencies
apt-get update
apt-get install -y libncurses5-dev libncursesw5-dev curl tar pigz make
sudo apt-get install python3-pip
sudo apt install -y golang-1.23

# sudo apt install -y python3-venv

# Create and activate virtual environment
#echo "Setting up virtual environment..."
#if [ ! -d ".venv" ]; then
#    python3 -m venv .venv
#fi

#if [ -d ".venv" ]; then
#  source .venv/bin/activate
#fi

# Install python dependencies
#echo "Installing Python dependencies..."
#pip3 install -r requirements.txt

# Install opkg-make-index
if [ ! -f "/tmp/openwrt-sdk/staging_dir/host/bin/opkg-make-index" ]; then
    echo "Installing opkg-make-index..."
    mkdir -p "/tmp/openwrt-sdk/staging_dir/host/bin"
    wget https://raw.githubusercontent.com/shr-project/opkg-utils/master/opkg-make-index -O "/tmp/openwrt-sdk/staging_dir/host/bin/opkg-make-index"
    chmod +x "/tmp/openwrt-sdk/staging_dir/host/bin/opkg-make-index"
else
    echo "opkg-make-index is already installed."
fi

# Install noscl
if ! [ -x "/usr/local/bin/noscl" ]; then
    echo "Installing noscl..."
    #GOBIN=/usr/local/bin go install github.com/fiatjaf/noscl@latest
    GOBIN=go install github.com/fiatjaf/noscl@latest
    # Create nostr config directory for both root and original user
    ORIGINAL_USER=$(logname)
    mkdir -p /root/.config/nostr
    mkdir -p /home/$ORIGINAL_USER/.config/nostr
    chown $ORIGINAL_USER:$ORIGINAL_USER /home/$ORIGINAL_USER/.config/nostr
    # Wait for the binary to be available
    sleep 2
fi

# Configure noscl
if [ -f "blossom_secrets.json" ]; then
    SECRET_KEY=$(jq -r '.secret_key_hex' blossom_secrets.json)
    /usr/local/bin/noscl setprivate "$SECRET_KEY"
else
    echo "Warning: blossom_secrets.json not found"
fi

# Add relays from blossom_secrets.json
if [ -f "blossom_secrets.json" ]; then
    while IFS= read -r relay; do
        if [ ! -z "$relay" ]; then
            echo "Adding relay: $relay"
            /usr/local/bin/noscl relay add "$relay"
        fi
    done < <(jq -r '.relays[]' blossom_secrets.json)
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

sudo apt-get install -y gawk coreutils curl tar qemu-system-arm qemu-system-mips socat
pip install requests nostr wheel

# Verify setup
echo "Setup complete. Verifying configuration..."
echo "Configured relays:"
/usr/local/bin/noscl relay
echo "Your public key:"
/usr/local/bin/noscl public

echo "Installation complete. The noscl binary is now available system-wide in /usr/local/bin"
