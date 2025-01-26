#!/bin/bash

# Require root privileges
if [ "$EUID" -ne 0 ]; then
    echo "Please run with sudo"
    exit 1
fi

# Preserve the original user's GOPATH and set environment
ORIGINAL_USER=$(logname)
export GOPATH="/home/$ORIGINAL_USER/go"
export PATH="$PATH:/usr/local/go/bin:$GOPATH/bin"

# Install noscl
echo "Installing noscl..."
GOBIN=/usr/local/bin go install github.com/fiatjaf/noscl@latest

# Create nostr config directory for both root and original user
mkdir -p /root/.config/nostr
mkdir -p /home/$ORIGINAL_USER/.config/nostr
chown $ORIGINAL_USER:$ORIGINAL_USER /home/$ORIGINAL_USER/.config/nostr

# Wait for the binary to be available
sleep 2

# Extract and set private key from blossom_secrets.json
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

# Verify setup
echo "Setup complete. Verifying configuration..."
echo "Configured relays:"
/usr/local/bin/noscl relay
echo "Your public key:"
/usr/local/bin/noscl public

echo "Installation complete. The noscl binary is now available system-wide in /usr/local/bin"
