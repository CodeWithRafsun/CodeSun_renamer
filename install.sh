#!/usr/bin/env bash

echo "Installing RENAMER tool..."
echo "=================================="

# Get current directory where project is
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Detect Termux or Linux
if [ -d "/data/data/com.termux/files/usr" ]; then
    BIN_DIR="/data/data/com.termux/files/usr/bin"
    echo "Detected: Termux"
else
    BIN_DIR="/usr/local/bin"
    echo "Detected: Linux"
fi

# Check if renamer executable exists
if [ ! -f "$DIR/renamer" ]; then
    echo "Error: 'renamer' executable not found in $DIR"
    echo "Make sure you are running install.sh from project root"
    exit 1
fi

# Copy renamer to bin directory
echo "Copying 'renamer' to $BIN_DIR..."
cp "$DIR/renamer" "$BIN_DIR/renamer"

# Make it executable
chmod +x "$BIN_DIR/renamer"

# Copy project to user home for main.py access
INSTALL_DIR="$HOME/.renamer"
echo "Copying project files to $INSTALL_DIR..."
rm -rf "$INSTALL_DIR"
mkdir -p "$INSTALL_DIR"
cp -r "$DIR"/* "$INSTALL_DIR/"

# Update renamer script path
sed -i "s|DIR=\"\$(cd \"\$(dirname \"\${BASH_SOURCE\[0\]}\")\" && pwd)\"|DIR=\"$INSTALL_DIR\"|" "$BIN_DIR/renamer"

echo "=================================="
echo "Installation Complete!"
echo "Now you can run 'renamer' from any directory"
echo "Try: renamer"
echo "=================================="
