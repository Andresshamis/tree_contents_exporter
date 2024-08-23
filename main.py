import os
import subprocess
import fnmatch

def generate_tree_with_contents(directory, output_file):
    # Define a blacklist of directories and file patterns to ignore
    blacklist_dirs = ['__pycache__', '.git', 'venv', '.venv', 'node_modules', 'env', '.idea', '.mypy_cache', '.pytest_cache', 'dist', 'build']
    blacklist_files = ['*.db', '*.sqlite3', '*.log', '*.cache', '*.DS_Store', '*.env', '*.pyc', '*.pyo', '*.so', '*.egg-info', '*.lock', '*.bak', '*.tmp']

    # Generate directory structure, excluding blacklisted directories
    tree_structure = subprocess.check_output(['tree', '-I', '|'.join(blacklist_dirs), directory]).decode('utf-8')

    with open(output_file, 'w') as f:
        # Write the directory structure to the file
        f.write(tree_structure + '\n\n')

        # Traverse the directory
        for root, dirs, files in os.walk(directory):
            # Modify dirs in-place to exclude blacklisted directories
            dirs[:] = [d for d in dirs if d not in blacklist_dirs]
            
            for file in files:
                # Skip blacklisted file patterns
                if any(fnmatch.fnmatch(file, pattern) for pattern in blacklist_files):
                    continue

                file_path = os.path.join(root, file)
                f.write(f'{file_path}:\n\n')
                try:
                    with open(file_path, 'r') as file_content:
                        contents = file_content.read()
                        f.write(contents + '\n\n\n')
                except Exception as e:
                    f.write(f'Error reading {file_path}: {e}\n\n\n')

if __name__ == "__main__":
    directory = input("Enter the directory to process: ")
    output_file = "directory_with_contents.txt"
    generate_tree_with_contents(directory, output_file)
    print(f"Directory structure and file contents written to {output_file}")
