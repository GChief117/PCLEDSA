import os
import sys
import time

# Function to insert a file into an array (simulating file insertion)
def insert_file_into_array(array, file_path):
    try:
        file_size = os.path.getsize(file_path)
    except OSError:
        print(f"Error retrieving file size for {file_path}")
        return
    
    # Start timing the insertion
    start_time = time.time()

    array.append((file_path, file_size))

    end_time = time.time()
    print(f"Time taken for array file insertion: {end_time - start_time:.6f} seconds")
    print(f"Time complexity: O(1)")

# Function to traverse the directory and collect files using arrays
def traverse_directory_for_array(root_directory):
    array = []

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                array.append((file_path, file_size))
            except OSError:
                continue

    end_time = time.time()
    print(f"Time taken for directory traversal: {end_time - start_time:.6f} seconds")

    # Measure space complexity for array
    space_used_array = sys.getsizeof(array)
    print(f"Space complexity for array: {space_used_array} bytes")

    return array

# Main function to perform file insertion into array
def run_file_insertion_with_array(root_directory, file_to_insert):
    # Traverse the directory and collect files
    array = traverse_directory_for_array(root_directory)

    # Insert the new file into the array
    print(f"\nInserting {file_to_insert} into the array:")
    insert_file_into_array(array, file_to_insert)

# Example usage for array file insertion
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    file_to_insert = "/path/to/new/file.txt"  # Replace with the path of the new file
    run_file_insertion_with_array(root_directory, file_to_insert)
