import os
import sys
import time

# Linear Search function
def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index
    return -1

# Function to collect paths into an array
def collect_paths_array(root_directory):
    paths = []
    for dirpath, dirnames, filenames in os.walk(root_directory):
        paths.append(dirpath)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            paths.append(file_path)
    return paths

# Apply linear search on the array and measure space and time complexity
def apply_linear_search_array(root_directory, target):
    paths = collect_paths_array(root_directory)

    # Measure space complexity
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes (for the array)")

    # Measure time complexity
    start_time = time.time()
    index = linear_search(paths, target)
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to perform linear search: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n)")

    if index != -1:
        print(f"Target found at index {index}: {paths[index]}")
    else:
        print("Target not found")

# Example usage for arrays
root_directory = "/Volumes/CD/pCLE"  # Adjust based on your root directory
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_linear_search_array(root_directory, target)
