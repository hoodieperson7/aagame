import os
from pathlib import Path

def is_binary(file_path):
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            if b'\0' in chunk:
                return True
            
        text_chars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
        return bool(chunk.translate(None, text_chars))
    except:
        return True

def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except:
        return 0

def count_loc(directory, exclude_common=True):
    total_files = 0
    total_lines = 0
    
    excluded = {'.venv', 'venv', 'env', 'node_modules', '.git', '__pycache__', 
                'site-packages', 'dist', 'build', '.eggs'}
    
    for root, dirs, files in os.walk(directory):
        if exclude_common:
            dirs[:] = [d for d in dirs if d not in excluded and not d.startswith('.')]
        
        for file in files:
            file_path = Path(root) / file
            
            if file_path.suffix != '.py':
                continue
            
            if is_binary(file_path):
                continue
            
            lines = count_lines(file_path)
            if lines == 0:
                continue
            
            total_files += 1
            total_lines += lines
    
    return total_files, total_lines

def main():
    directory = input("Enter directory path (or '.' for current): ").strip() or '.'
    
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory")
        return
    
    exclude_dirs = input("Exclude common dirs? (venv, node_modules, .git) [Y/n]: ").strip().lower()
    exclude = exclude_dirs != 'n'
    
    print(f"\nScanning Python files in {directory}...\n")
    total_files, total_lines = count_loc(directory, exclude)
    
    print(f"Python files: {total_files}")
    print(f"Total lines:  {total_lines:,}")

if __name__ == "__main__":
    main()