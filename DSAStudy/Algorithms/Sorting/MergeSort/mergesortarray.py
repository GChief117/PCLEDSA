import os
import time
import sys

# Merge function to merge two sorted subarrays
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# MergeSort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Function to collect all paths in the directory
def collect_paths(root_directory):
    paths = []
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Add the directory path
        paths.append(dirpath)
        # Add each file path in the directory
        for filename in filenames:
            paths.append(os.path.join(dirpath, filename))
    return paths

# Function to apply MergeSort to the directory structure and measure complexities
def merge_sort_directory(root_directory):
    # Step 1: Collect all paths
    paths = collect_paths(root_directory)

    # Measure space complexity before sorting
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes (for the list of paths)")

    # Step 2: Apply MergeSort and measure time taken
    start_time = time.time()
    sorted_paths = merge_sort(paths)
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to apply MergeSort: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n log n)")

    # Output sorted paths
    for path in sorted_paths:
        print(f"Processing path: {path}")

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with the actual root directory path
merge_sort_directory(root_directory)
