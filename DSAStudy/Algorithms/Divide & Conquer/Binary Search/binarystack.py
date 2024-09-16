import os
import sys
import time

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def to_list(self):
        return self.stack

# Binary search function for stack (converted to sorted list)
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

# Function to traverse the directory and push file sizes into a stack
def traverse_directory_for_stack(root_directory):
    stack = Stack()

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                stack.push(file_size)
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for stack
    space_used_stack = sys.getsizeof(stack)
    print(f"Space complexity for stack: {space_used_stack} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return stack

# Main function for binary search with stack
def run_binary_search_with_stack(root_directory):
    # Traverse the directory and collect file sizes
    stack = traverse_directory_for_stack(root_directory)

    # Convert stack to a sorted list
    sorted_weights = sorted(stack.to_list())

    # Perform binary search
    binary_search(sorted_weights)

# Example usage for binary search with stack
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_binary_search_with_stack(root_directory)
