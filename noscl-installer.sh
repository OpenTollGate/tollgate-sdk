#!/bin/bash

# Install noscl
go install github.com/fiatjaf/noscl@latest

# Add Go binary path to PATH for current session
export PATH=$PATH:$HOME/go/bin

# Add Go binary path to PATH permanently
if ! grep -q "export PATH=\$PATH:\$HOME/go/bin" ~/.bashrc; then
    echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc
    source ~/.bashrc
fi

# Create nostr config directory
mkdir -p ~/.config/nostr

# Extract and set private key from blossom_secrets.json
SECRET_KEY=$(jq -r '.secret_key_hex' blossom_secrets.json)
noscl setprivate "$SECRET_KEY"

# Add relays from blossom_secrets.json
while IFS= read -r relay; do
    if [ ! -z "$relay" ]; then
        echo "Adding relay: $relay"
        noscl relay add "$relay"
    fi
done < <(jq -r '.relays[]' blossom_secrets.json)

# Verify setup
echo "Setup complete. Verifying configuration..."
echo "Configured relays:"
noscl relay
echo "Your public key:"
noscl public

echo "Installation complete. If noscl is still not found, please run:"
echo "export PATH=\$PATH:\$HOME/go/bin"
echo "or restart your terminal"
