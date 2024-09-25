import os
import sys
import time

# Function to collect all paths in the directory and report complexities
def collect_paths_and_complexities(root_directory):
    all_paths = []  # Initialize an empty array to store paths
    
    # Start timing the directory traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Add the directory path to the array
        all_paths.append(dirpath)
        
        # Add each file in the directory to the array
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            all_paths.append(file_path)

    # End timing
    end_time = time.time()
    
    # Calculate time taken for traversal
    traversal_time = end_time - start_time
    
    # Calculate space complexity (size of the array)
    space_complexity = sys.getsizeof(all_paths)

    # Output only the Directory Traversal information in the correct format
    print(f"Directory Traversal, O(n), O(n), {traversal_time:.6f} seconds, {space_complexity} bytes")

    return all_paths

# Main function
def main():
    # Define the root directory (adjust this to your actual directory path)
    root_directory = "/Volumes/CD/pCLE"
    
    # Collect all paths and output the traversal complexities
    collect_paths_and_complexities(root_directory)

# Run the main function
if __name__ == "__main__":
    main()
