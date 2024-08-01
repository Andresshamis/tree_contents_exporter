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

if __name__ == "__main__":
    directory = input("Enter the directory to process: ")
    output_file = "directory_with_contents.txt"
    generate_tree_with_contents(directory, output_file)
    print(f"Directory structure and file contents written to {output_file}")
