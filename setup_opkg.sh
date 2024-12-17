#!/bin/bash
set -e

# Clone opkg-utils if it doesn't exist
if [ ! -d "opkg-utils" ]; then
    git clone https://github.com/shr-project/opkg-utils.git
fi

# Copy the setup file over
cp setup_opkg.py opkg-utils/setup.py

# Install it in editable mode
cd opkg-utils
pip install -e .
