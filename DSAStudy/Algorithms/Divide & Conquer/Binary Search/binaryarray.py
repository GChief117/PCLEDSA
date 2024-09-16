import os
import sys
import time

# Binary search function
def binary_search(sorted_weights):
    low, high = 0, len(sorted_weights) - 1

    # Start timing the binary search
    start_time = time.time()

    while low <= high:
        mid = (low + high) // 2
        # Since we have no specific target, print the middle element
        print(f"Processing file size at index {mid}: {sorted_weights[mid]} bytes")
        low = mid + 1

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to perform binary search: {time_taken:.6f} seconds")
    print(f"Time complexity: O(log n), where n = {len(sorted_weights)}")

# Function to traverse the directory and collect file sizes
def traverse_directory_for_array(root_directory):
    weights = []

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                weights.append(file_size)
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for storing file sizes
    space_used_weights = sys.getsizeof(weights)
    print(f"Space complexity for storing file sizes: {space_used_weights} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return weights

# Main function for binary search with array
def run_binary_search_with_array(root_directory):
    # Traverse the directory and collect file sizes
    weights = traverse_directory_for_array(root_directory)

    # Sort the file sizes
    sorted_weights = sorted(weights)

    # Perform binary search on sorted weights
    binary_search(sorted_weights)

# Example usage for binary search with array
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_binary_search_with_array(root_directory)
