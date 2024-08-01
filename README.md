# Directory Tree and File Contents Extractor

This project provides a Python script that generates a visual representation of a directory's structure and extracts the contents of all text files within the directory. The generated output is saved in a text file. This tool can be useful for developers who want to document the structure and contents of a project directory, or for anyone who needs an overview of files and their contents in a specified directory.

## How It Works

The script performs the following tasks:
1. **Generates Directory Structure:** It uses the `tree` command to create a visual representation of the directory structure.
2. **Extracts File Contents:** It traverses the directory, reads the contents of all files, and appends them to the output file.

## Usage

### Running the Script

1. **Input Directory:** When prompted, enter the path of the directory you want to process.
2. **Output File:** The output will be written to a file named `directory_with_contents.txt` in the current working directory.

### Output

The output file `directory_with_contents.txt` will contain:
- A tree-like structure representing the directory.
- The contents of each file in the directory, printed below the corresponding file path.

## Code Overview

```python
import os
import subprocess

def generate_tree_with_contents(directory, output_file):
    # Generate directory structure
    tree_structure = subprocess.check_output(['tree', directory]).decode('utf-8')

    with open(output_file, 'w') as f:
        # Write the directory structure to the file
        f.write(tree_structure + '\n\n')
        
        # Traverse the directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                f.write(f'{file_path}:\n\n')
                try:
                    with open(file_path, 'r') as file_content:
                        contents = file_content.read()
                        f.write(contents + '\n\n\n')
                except Exception as e:
                    f.write(f'Error reading {file_path}: {e}\n\n\n')

directory = input("Enter the directory to process: ")
output_file = "directory_with_contents.txt"
generate_tree_with_contents(directory, output_file)
print(f"Directory structure and file contents written to {output_file}")
```

## Notes

- Ensure that the `tree` command is installed and available in your system's PATH, as the script relies on it to generate the directory structure.
- This script assumes all files can be opened and read as text files. Binary files or files with restricted access may cause errors, which are caught and noted in the output.

## License

This project is available for use under a permissive license. You are free to use, modify, and distribute the code for any purpose. If you utilize this project in educational materials, social media, tutorials, or any other form of publication, please provide appropriate credit by citing the project.