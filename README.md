README.md পুরোটা:

# CodeSun Renamer ⚡

A lightweight and powerful CLI bulk file renaming utility built with pure Python.

No external libraries.
No API dependency.
Fast, simple, and developer friendly terminal file management tool.

---

## ✨ Features

### Basic Rename Features

### 1. Batch Prefix Rename

Rename multiple files with automatic numbering.

Example:

Before:

photo.jpg image.jpg test.jpg

After:

file_001.jpg file_002.jpg file_003.jpg

---

### 2. Find & Replace Rename

Replace specific text from filenames.

Example:

Before:

vacation_photo.jpg

After:

trip_photo.jpg

---

### 3. Add Date Rename

Automatically add current date to filenames.

Example:

photo.jpg

↓

2026-06-22_photo.jpg

---

### 4. Undo Rename

Restore the previous rename operation using rename history.

---

# 🚀 Advanced Features (v2.0.1)

## Prefix + Suffix Rename

Add custom prefix and suffix.

Example:

photo.jpg

↓

new_photo_backup.jpg

---

## Filename Case Converter

Convert filename format:

Available modes:

- lowercase
- UPPERCASE
- Title Case


Example:

My Photo File.jpg

↓

my photo file.jpg

---

## Remove Text From Filename

Remove unwanted text from filenames.

Example:

old_photo_backup.jpg

↓

photo_backup.jpg

---

## Extension Converter

Change file extensions easily.

Example:

image.jpg

↓

image.png

---

# 📦 Installation

Clone repository:

```bash
git clone YOUR_REPOSITORY_URL

Go to project folder:

cd CodeSun_renamer

Run installer:

./install.sh

or:

bash install.sh

After successful installation:

renamer


---

🗑 Uninstall

Run:

./uninstall.sh


---

💻 Supported Platforms

Linux

Termux Android



---

🛠 Commands

Inside CodeSun Renamer:

/help

Show available commands.

/about

Show project information.

/version

Show current version.

/clear

Clear terminal.

/quit

Exit application.


---

📁 Project Structure

CodeSun_renamer

├── assets
│   ├── brand.txt
│   ├── banner.txt
│   └── success.txt
│
├── core
│   └── renamer_logic.py
│
├── utils
│   └── helpers.py
│
├── main.py
├── install.sh
├── uninstall.sh
└── renamer


---

⚙️ Technical Information

Language: Python 3

External dependency: None

Interface: Terminal CLI

Lightweight and portable

Designed for Linux and Termux



---

📌 Version

Current Version:

v2.0.1


---

👨‍💻 Developer

Mahedi Hasan Rafsun

Powered by CodeSun


---

Made with Python ⚡
