import os
import time
import sys

# Heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# HeapSort function
def heap_sort(arr):
    n = len(arr)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr

# Collect all paths in the directory into an array
def collect_paths_array(root_directory):
    paths = []
    for dirpath, dirnames, filenames in os.walk(root_directory):
        paths.append(dirpath)
        for filename in filenames:
            paths.append(os.path.join(dirpath, filename))
    return paths

# Apply HeapSort to the array and measure complexities
def heap_sort_array(root_directory):
    # Step 1: Collect all paths
    paths = collect_paths_array(root_directory)

    # Measure space complexity before sorting
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes (for the array)")

    # Measure time taken to apply HeapSort
    start_time = time.time()
    sorted_paths = heap_sort(paths)
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to apply HeapSort: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n log n)")

    # Output sorted paths
    for path in sorted_paths:
        print(f"Processing path: {path}")

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory path
heap_sort_array(root_directory)
