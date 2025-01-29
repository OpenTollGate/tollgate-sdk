#!/bin/bash
set -e

# Install system dependencies
apt-get update
apt-get install -y libncurses5-dev libncursesw5-dev curl tar pigz

# Create and activate virtual environment
echo "Setting up virtual environment..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
source .venv/bin/activate

# Install python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

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
    GOBIN=/usr/local/bin go install github.com/fiatjaf/noscl@latest
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

sudo apt-get install -y gawk coreutils curl tar qemu-system-arm qemu-system-mips socat
pip3 install requests nostr


# Verify setup
echo "Setup complete. Verifying configuration..."
echo "Configured relays:"
/usr/local/bin/noscl relay
echo "Your public key:"
/usr/local/bin/noscl public

echo "Installation complete. The noscl binary is now available system-wide in /usr/local/bin"
