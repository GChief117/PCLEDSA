import os

# Function to collect all paths in the directory into an array
def collect_paths_into_array(root_directory):
    all_paths = []  # Initialize an empty array to store paths
    
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Add the directory path to the array
        all_paths.append(dirpath)
        
        # Add each file in the directory to the array
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            all_paths.append(file_path)

    return all_paths

# Main function
def main():
    # Define the root directory (adjust this to your actual directory path)
    root_directory = "/Volumes/CD/pCLE"
    
    # Collect all paths into an array
    all_paths = collect_paths_into_array(root_directory)
    
    # Output the paths (you can remove this part if you don't want to print them)
    for path in all_paths:
        print(path)
    
    # Optionally return the array for further processing
    return all_paths

# Run the main function
if __name__ == "__main__":
    main()
