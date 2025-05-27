import os

def traverse_directory_tree(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"Current Directory: {dirpath}")
        
        if dirnames:
            print("Subdirectories:")
            for dirname in dirnames:
                print(f"  - {dirname}")
        else:
            print("No subdirectories.")
        
        if filenames:
            print("Files:")
            for filename in filenames:
                print(f"  - {filename}")
        else:
            print("No files.")
        
        print("=" * 40)

# Set root directory to current folder
root_directory = "C:/External/Nanna/Code/R"

# Run the function
traverse_directory_tree(root_directory)
