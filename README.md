# LimitTree

This is a custom tree command implemented in Python, which allows users to display directory structures with depth (`n`) and file limits (`m`).

## Features
- Display directory structure up to a specified depth (`n`).
- Limit the number of files displayed per folder to `m`.
- Works on macOS, Linux, and Windows (with WSL or Python environment).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/koi-ama/LimitTree.git
   ```

2. **Navigate to the repository directory**:
   ```bash
   cd LimitTree
   ```
3. **Make the installation script executable**:
   Before running the installation script, make sure it has execution permissions.
   ```bash
   chmod +x install.sho
```
4. **Run the installation script**:
   The `install.sh` script will install the `tree` command so that you can use `tree n m`.
   ```bash
   sudo ./install.sh
   ```

## Usage

Once installed, use the `tree` command to display directory structures with depth (`n`) and file limit (`m`). Example usage:
```bash
tree 4 3
```

This will display the directory structure up to a depth of 4, showing a maximum of 3 files per folder. The output will show the directory structure in a clean, hierarchical format, making it easy to browse through large file systems.

### Arguments:

- `n`: The maximum depth of the directory tree to display.
- `m`: The maximum number of files to display in each folder. Folders are not limited by this value.

## Requirements

- Python 3.x must be installed on your system.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
