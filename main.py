#!/usr/bin/env python3
import os
import sys
import signal

# Add project folders to import path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.renamer_logic import (
    batch_prefix_rename,
    find_replace_rename, 
    add_date_rename,
    undo_last_rename
)
from utils.helpers import (
    validate_folder,
    validate_extension,
    validate_number,
    get_file_count
)

# Colors
CYAN = '\033[0;36m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
BOLD = '\033[1m'
NC = '\033[0m'

def handle_exit(signum, frame):
    print(f"\n\n{GREEN}Thanks for using RENAMER! Powered by CodeSun ✨{NC}")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)

def load_banner():
    banner_path = os.path.join(os.path.dirname(__file__), "assets", "banner.txt")
    try:
        with open(banner_path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return "RENAMER\n"

def show_menu():
    print(CYAN + load_banner() + NC)
    print(GREEN + "="*60 + NC)
    print(f"{BOLD} 1. {CYAN}Batch Prefix Rename{NC} - file_1.jpg, file_2.jpg")
    print(f"{BOLD} 2. {YELLOW}Find & Replace{NC} - 'vacation' -> 'trip'")
    print(f"{BOLD} 3. {GREEN}Add Date to Filename{NC} - 2026-06-17_file.jpg")
    print(f"{BOLD} 4. {RED}Undo Last Rename{NC}")
    print(f"{BOLD} 5. Exit")
    print(GREEN + "="*60 + NC)
    print(YELLOW + " Type '/quit' to exit anytime" + NC)

def get_valid_folder():
    while True:
        folder = input(f"\n{YELLOW}Enter folder path: {NC}").strip()
        if folder.lower() == "/quit":
            return None
        
        valid, error = validate_folder(folder)
        if valid:
            count = get_file_count(folder)
            print(f"{GREEN}Found {count} files in folder{NC}")
            return folder
        else:
            print(RED + error + NC)

def mode_1_prefix():
    folder = get_valid_folder()
    if not folder: return
    
    prefix = input(f"{YELLOW}Enter prefix [default: file]: {NC}").strip() or "file"
    
    ext_input = input(f"{YELLOW}Filter by extension [.jpg .txt] or Enter for all: {NC}").strip()
    valid, ext = validate_extension(ext_input)
    if not valid:
        print(RED + ext + NC)
        ext = None
    
    start_input = input(f"{YELLOW}Start number [default: 1]: {NC}").strip()
    start, msg = validate_number(start_input, 1, 1, 9999)
    if msg: print(YELLOW + msg + NC)
    
    padding_input = input(f"{YELLOW}Padding [default: 3 for 001]: {NC}").strip()
    padding, msg = validate_number(padding_input, 3, 1, 10)
    if msg: print(YELLOW + msg + NC)
    
    print(f"\n{CYAN}Example: photo.jpg -> {prefix}_{str(start).zfill(padding)}.jpg{NC}")
    batch_prefix_rename(folder, prefix, ext, start, padding)

def mode_2_replace():
    folder = get_valid_folder()
    if not folder: return
    
    find_text = input(f"{YELLOW}Enter text to find: {NC}").strip()
    if not find_text:
        print(RED + "Error: Find text cannot be empty!" + NC)
        return
    
    replace_text = input(f"{YELLOW}Enter text to replace with: {NC}").strip()
    
    ext_input = input(f"{YELLOW}Filter by extension or Enter for all: {NC}").strip()
    valid, ext = validate_extension(ext_input)
    if not valid:
        print(RED + ext + NC)
        ext = None
    
    print(f"\n{CYAN}Example: vacation_photo.jpg -> {replace_text}_photo.jpg{NC}")
    find_replace_rename(folder, find_text, replace_text, ext)

def mode_3_date():
    folder = get_valid_folder()
    if not folder: return
    
    ext_input = input(f"{YELLOW}Filter by extension or Enter for all: {NC}").strip()
    valid, ext = validate_extension(ext_input)
    if not valid:
        print(RED + ext + NC)
        ext = None
    
    print(f"\n{CYAN}Example: photo.jpg -> 2026-06-17_photo.jpg{NC}")
    add_date_rename(folder, ext)

def mode_4_undo():
    folder = get_valid_folder()
    if not folder: return
    
    undo_last_rename(folder)

def main():
    while True:
        os.system("clear")
        show_menu()
        choice = input(f"\n{BOLD}Select option 1-5: {NC}").strip()

        if choice.lower() == "/quit" or choice == "5":
            print(f"\n{GREEN}Thanks for using RENAMER! Powered by CodeSun ✨{NC}")
            sys.exit(0)
        elif choice == "1":
            mode_1_prefix()
            input(f"\n{YELLOW}Press Enter to return to menu...{NC}")
        elif choice == "2":
            mode_2_replace()
            input(f"\n{YELLOW}Press Enter to return to menu...{NC}")
        elif choice == "3":
            mode_3_date()
            input(f"\n{YELLOW}Press Enter to return to menu...{NC}")
        elif choice == "4":
            mode_4_undo()
            input(f"\n{YELLOW}Press Enter to return to menu...{NC}")
        else:
            print(RED + "Invalid input! Please enter 1-5" + NC)
            input(f"{YELLOW}Press Enter...{NC}")

if __name__ == "__main__":
    main()
