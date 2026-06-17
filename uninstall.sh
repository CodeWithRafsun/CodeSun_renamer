#!/usr/bin/env bash

echo "Uninstalling RENAMER tool..."
echo "=================================="

# Detect Termux or Linux
if [ -d "/data/data/com.termux/files/usr" ]; then
    BIN_DIR="/data/data/com.termux/files/usr/bin"
    echo "Detected: Termux"
else
    BIN_DIR="/usr/local/bin"
    echo "Detected: Linux"
fi

# Remove global command
if [ -f "$BIN_DIR/renamer" ]; then
    echo "Removing 'renamer' from $BIN_DIR..."
    rm "$BIN_DIR/renamer"
    echo "✓ Global command removed"
else
    echo "Global command not found"
fi

# Remove project files from home
INSTALL_DIR="$HOME/.renamer"
if [ -d "$INSTALL_DIR" ]; then
    echo "Removing project files from $INSTALL_DIR..."
    rm -rf "$INSTALL_DIR"
    echo "✓ Project files removed"
else
    echo "Project files not found"
fi

echo "=================================="
echo "Uninstallation Complete!"
echo "RENAMER has been removed from your system"
echo "=================================="
