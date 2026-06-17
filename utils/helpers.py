import os
import re

def validate_folder(path):
    """Check if folder exists and is accessible"""
    if not path or not path.strip():
        return False, "Error: Folder path cannot be empty"
    
    path = path.strip()
    
    if not os.path.exists(path):
        return False, "Error: Folder does not exist"
    
    if not os.path.isdir(path):
        return False, "Error: Path is not a directory"
    
    if not os.access(path, os.R_OK):
        return False, "Error: No read permission for this folder"
    
    if not os.access(path, os.W_OK):
        return False, "Error: No write permission for this folder"
    
    return True, None

def validate_extension(ext):
    """Validate file extension format"""
    if not ext:
        return True, None
    
    ext = ext.strip()
    if not ext.startswith('.'):
        ext = '.' + ext
    
    # Only allow alphanumeric + dot
    if not re.match(r'^\.[a-zA-Z0-9]+$', ext):
        return False, "Error: Invalid extension format. Use .jpg or jpg"
    
    return True, ext.lower()

def validate_number(value, default=1, min_val=1, max_val=999):
    """Validate number input with default"""
    if not value or not value.strip():
        return default, None
    
    try:
        num = int(value.strip())
        if num < min_val or num > max_val:
            return default, f"Number must be between {min_val} and {max_val}. Using default: {default}"
        return num, None
    except ValueError:
        return default, f"Invalid number. Using default: {default}"

def get_file_count(folder_path, extension=None):
    """Get total file count for info display"""
    if extension:
        if not extension.startswith('.'):
            extension = '.' + extension
        files = [f for f in os.listdir(folder_path) 
                 if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(extension)]
    else:
        files = [f for f in os.listdir(folder_path) 
                 if os.path.isfile(os.path.join(folder_path, f))]
    return len(files)

def format_size(size_bytes):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"
