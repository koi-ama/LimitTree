#!/usr/bin/env python3
import os
import argparse

# ANSI escape sequences for colors
CYAN = '\033[38;5;45m'  # Bright cyan/blue in 256 color mode
RED = '\033[38;5;196m'  # Bright red in 256 color mode
RESET = '\033[0m'

# Global counters for directories, files, and skipped files
folder_count = 0
file_count = 0
skipped_file_count = 0

def print_tree(dir_path, indent="", level=0, max_depth=None, max_files=None, show_hidden=False):
    global folder_count, file_count, skipped_file_count

    # If max_depth is not None, stop the recursion when the level exceeds the max depth
    if max_depth is not None and level >= max_depth:
        return

    # Retrieve items in the directory, and separate directories and files
    items = os.listdir(dir_path)
    if not show_hidden:
        # Filter out hidden files if -a option is not specified
        items = [item for item in items if not item.startswith('.')]
    items = sorted(items)  # Sort items alphabetically

    # Separate directories and files into different lists
    dirs = [item for item in items if os.path.isdir(os.path.join(dir_path, item))]
    files = [item for item in items if os.path.isfile(os.path.join(dir_path, item))]

    # Display directories
    for i, folder in enumerate(dirs):
        connector = "└── " if i == len(dirs) - 1 and len(files) == 0 else "├── "
        full_path = os.path.join(dir_path, folder)
        print(indent + connector + CYAN + folder + RESET)
        folder_count += 1

        # Recursively print the contents if the item is a directory
        next_indent = indent + ("    " if i == len(dirs) - 1 and len(files) == 0 else "│   ")
        print_tree(full_path, next_indent, level + 1, max_depth, max_files, show_hidden)

    # Display files (up to max_files)
    files_to_display = files[:max_files] if max_files is not None else files
    for i, file in enumerate(files_to_display):
        connector = "└── " if i == len(files_to_display) - 1 else "├── "
        full_path = os.path.join(dir_path, file)
        print(indent + connector + file)
        file_count += 1

    # If there are more files than max_files, print a message in red
    remaining_files = len(files) - len(files_to_display)
    if remaining_files > 0:
        print(indent + RED + f"... {remaining_files} more file(s) hidden" + RESET)
        skipped_file_count += remaining_files

    # Add an extra empty line to visually separate directories and files
    if len(files) > 0 or len(dirs) > 0:
        print(indent.rstrip())

if __name__ == "__main__":
    # Process command line arguments
    parser = argparse.ArgumentParser(description="Display directory structure in a tree format.")
    parser.add_argument("max_depth", type=int, nargs='?', default=0, help="The maximum depth of directories to display. Use 0 for unlimited.")
    parser.add_argument("max_files", type=int, nargs='?', default=None, help="The maximum number of files to display in each directory. Directories are not limited.")
    parser.add_argument("-a", "--all", action="store_true", help="Show hidden files (those starting with a dot)")

    # Get the arguments
    args = parser.parse_args()
    
    # Set max_depth and max_files
    max_depth = None if args.max_depth == 0 else args.max_depth
    max_files = args.max_files

    # Display the current working directory
    directory = os.getcwd()
    print(directory)
    
    # Display the directory structure, considering hidden files option
    print_tree(directory, max_depth=max_depth, max_files=max_files, show_hidden=args.all)
    
    # Print total counts of directories, files, and hidden files
    print(f"\n{folder_count} folders, {file_count} files found.")
    if skipped_file_count > 0:
        print(f"{RED}{skipped_file_count} files were hidden.{RESET}")

