import os
import sys
import time
from collections import deque

# Queue class using deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def to_list(self):
        return list(self.queue)

# Binary search function for queue (converted to sorted list)
def binary_search(sorted_weights):
    low, high = 0, len(sorted_weights) - 1

    # Start timing the binary search
    start_time = time.time()

    while low <= high:
        mid = (low + high) // 2
        print(f"Processing file size at index {mid}: {sorted_weights[mid]} bytes")
        low = mid + 1

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to perform binary search: {time_taken:.6f} seconds")
    print(f"Time complexity: O(log n), where n = {len(sorted_weights)}")

# Function to traverse the directory and enqueue file sizes into a queue
def traverse_directory_for_queue(root_directory):
    queue = Queue()

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                queue.enqueue(file_size)
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for queue
    space_used_queue = sys.getsizeof(queue)
    print(f"Space complexity for queue: {space_used_queue} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return queue

# Main function for binary search with queue
def run_binary_search_with_queue(root_directory):
    # Traverse the directory and collect file sizes
    queue = traverse_directory_for_queue(root_directory)

    # Convert queue to a sorted list
    sorted_weights = sorted(queue.to_list())

    # Perform binary search on sorted weights
    binary_search(sorted_weights)

# Example usage for binary search with queue
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_binary_search_with_queue(root_directory)
