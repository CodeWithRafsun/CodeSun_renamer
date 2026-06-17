import os
from datetime import datetime

def get_files(folder_path, extension=None):
    """Get all files from folder. Filter by extension if given."""
    if not os.path.isdir(folder_path):
        return None, "Error: Folder not found"
    
    files = [f for f in os.listdir(folder_path) 
             if os.path.isfile(os.path.join(folder_path, f))]
    files.sort()
    
    if extension:
        if not extension.startswith('.'):
            extension = '.' + extension
        files = [f for f in files if f.endswith(extension)]
    
    return files, None

def save_log(folder_path, log_data):
    """Save rename log for undo"""
    log_path = os.path.join(folder_path, "rename_log.txt")
    with open(log_path, "w", encoding="utf-8") as f:
        for old_path, new_path in log_data:
            f.write(f"{new_path}|{old_path}\n")

def load_log(folder_path):
    """Load rename log for undo"""
    log_path = os.path.join(folder_path, "rename_log.txt")
    if not os.path.exists(log_path):
        return None, "No log file found. Nothing to undo."
    
    log_data = []
    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            new_path, old_path = line.strip().split("|")
            log_data.append((new_path, old_path))
    return log_data, None

def preview_and_execute(folder_path, log_data):
    """Show preview then execute rename"""
    print("\n--- Preview ---")
    for old_path, new_path in log_data:
        old_name = os.path.basename(old_path)
        new_name = os.path.basename(new_path)
        print(f"{old_name} -> {new_name}")
    
    confirm = input("\nProceed with rename? y/n: ").lower().strip()
    if confirm != 'y':
        print("Cancelled.")
        return False
    
    # Execute rename
    for old_path, new_path in log_data:
        os.rename(old_path, new_path)
    
    save_log(folder_path, log_data)
    print(f"\nSuccess! {len(log_data)} files renamed.")
    print(f"Log saved to: rename_log.txt")
    return True

def batch_prefix_rename(folder_path, prefix="file", extension=None, start=1, padding=3):
    """Mode 1: file_001.jpg, file_002.jpg"""
    files, error = get_files(folder_path, extension)
    if error:
        return error
    
    if not files:
        return "No files found."
    
    log_data = []
    count = start
    
    for filename in files:
        name, ext = os.path.splitext(filename)
        new_name = f"{prefix}_{str(count).zfill(padding)}{ext}"
        
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        
        log_data.append((old_path, new_path))
        count += 1
    
    preview_and_execute(folder_path, log_data)
    return None

def find_replace_rename(folder_path, find_text, replace_text, extension=None):
    """Mode 2: vacation photo.jpg -> trip photo.jpg"""
    files, error = get_files(folder_path, extension)
    if error:
        return error
    
    if not files:
        return "No files found."
    
    log_data = []
    
    for filename in files:
        if find_text in filename:
            new_name = filename.replace(find_text, replace_text)
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            log_data.append((old_path, new_path))
    
    if not log_data:
        return f"No files contain '{find_text}'"
    
    preview_and_execute(folder_path, log_data)
    return None

def add_date_rename(folder_path, extension=None):
    """Mode 3: 2026-06-17_file.jpg"""
    files, error = get_files(folder_path, extension)
    if error:
        return error
    
    if not files:
        return "No files found."
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_data = []
    
    for filename in files:
        new_name = f"{date_str}_{filename}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        log_data.append((old_path, new_path))
    
    preview_and_execute(folder_path, log_data)
    return None

def undo_last_rename(folder_path):
    """Mode 4: Undo last operation"""
    log_data, error = load_log(folder_path)
    if error:
        return error
    
    print("\n--- Undo Preview ---")
    for new_path, old_path in log_data:
        new_name = os.path.basename(new_path)
        old_name = os.path.basename(old_path)
        print(f"{new_name} -> {old_name}")
    
    confirm = input("\nProceed with undo? y/n: ").lower().strip()
    if confirm != 'y':
        print("Cancelled.")
        return None
    
    for new_path, old_path in log_data:
        if os.path.exists(new_path):
            os.rename(new_path, old_path)
    
    os.remove(os.path.join(folder_path, "rename_log.txt"))
    print(f"\nUndo complete! {len(log_data)} files restored.")
    return None
