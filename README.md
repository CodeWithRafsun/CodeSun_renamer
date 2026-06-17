
# RENAMER

A powerful bulk file renaming tool for Termux and Linux. Rename hundreds of files in seconds with preview mode, undo support, and a clean colorful UI.

**Powered by CodeSun** | **Developed by Mahedi Hasan Rafsun**

## GitHub Repository

🔗 **Repository**: [github.com/codewithrafsun/codesun_renamer](https://github.com/codewithrafsun/codesun_renamer)  
👤 **Author**: [@codewithrafsun](https://github.com/codewithrafsun)

## Features

- **Batch Prefix Rename**: `file_001.jpg`, `file_002.jpg`, `file_003.jpg`
- **Find & Replace**: `vacation photo.jpg` → `trip photo.jpg`
- **Add Date Prefix**: `2026-06-17_filename.jpg`
- **Undo Last Operation**: Restore previous filenames with one command
- **Preview Before Rename**: See all changes before applying
- **Extension Filter**: Target specific file types like `.jpg`, `.txt`, `.pdf`
- **Colorful Interface**: Loading bar + colored banner + colored menu
- **100% Offline**: No internet required, no external dependencies
- **Ctrl+C Safe**: Graceful exit with custom thanks message
- **Global Command**: Run `renamer` from any directory after installation

## Quick Install

### One-Line Install for Termux/Linux
```bash
git clone https://github.com/codewithrafsun/codesun_renamer.git && cd codesun_renamer && chmod +x install.sh && ./install.sh
### Manual Installation
# Clone the repository
git clone https://github.com/codewithrafsun/codesun_renamer.git

# Enter project directory
cd codesun_renamer

# Make installer executable
chmod +x install.sh

# Run installer
./install.sh
### Run the Tool
renamer
### Update to Latest Version
cd codesun_renamer
git pull
./install.sh
### Uninstall
cd codesun_renamer
chmod +x uninstall.sh
./uninstall.sh
## Usage Guide

After installation, launch the tool:
renamer
### 1. Batch Prefix Rename
Rename multiple files with sequential numbers.
Select option 1-5: 1
Enter folder path: /storage/emulated/0/Download/photos
Enter prefix [default: file]: img
Filter by extension [.jpg .txt] or Enter for all: .jpg
Start number [default: 1]: 1
Padding [default: 3 for 001]: 3

Result: photo.jpg → img_001.jpg
### 2. Find & Replace
Replace text inside filenames.
Select option 1-5: 2
Enter folder path: ~/test
Enter text to find: vacation
Enter text to replace with: trip
Filter by extension or Enter for all: .jpg

Result: vacation_photo.jpg → trip_photo.jpg
### 3. Add Date to Filename
Add current date as prefix to all files.
Select option 1-5: 3
Enter folder path: /storage/emulated/0/DCIM/Camera
Filter by extension or Enter for all: .jpg

Result: photo.jpg → 2026-06-17_photo.jpg
### 4. Undo Last Rename
Restore filenames from the last operation.
Select option 1-5: 4
Enter folder path: ~/test
Preview shows old names → new names
Proceed with undo? y/n: y
### 5. Exit
Select option 1-5: 5
## Tips for Termux Users

*Common Folder Paths:*
- Internal Storage: `/storage/emulated/0/Download`
- DCIM Camera: `/storage/emulated/0/DCIM/Camera`
- WhatsApp Images: `/storage/emulated/0/WhatsApp/Media/WhatsApp Images`
- Home Directory: `~/`

*Exit Anytime*: Type `/quit` or press `Ctrl+C`

*Safety First*: Every rename operation shows a preview. Confirm with `y` to proceed.

## Project Structure
codesun_renamer/
├── renamer              # Bash executable - global command with loading bar
├── main.py              # Python entry point + menu + color interface
├── install.sh           # Installer script for Termux/Linux
├── uninstall.sh         # Uninstaller script
├── core/
│   ├── __init__.py
│   └── renamer_logic.py # Core renaming logic
├── utils/
│   ├── __init__.py
│   └── helpers.py       # Input validation and helper functions
├── assets/
│   └── banner.txt       # ASCII art banner with RENAMER logo
├── README.md
└── LICENSE              # MIT License
## Requirements

- Python 3.6 or higher
- Bash shell
- Termux or Linux system
- No external Python packages required

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact & Support

- GitHub: https://github.com/codewithrafsun
- Repository: https://github.com/codewithrafsun/codesun_renamer
- Email: codewithrafsun@gmail.com
- Website: http://codewithrafsun.vercel.app

---

If this tool saved you time, please star ⭐ the repository!
।
