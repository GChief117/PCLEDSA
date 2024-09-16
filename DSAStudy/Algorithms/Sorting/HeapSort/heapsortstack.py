import os
import time
import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    # HeapSort the stack
    def heap_sort_stack(self):
        # Convert stack to array
        arr = self.stack.copy()

        # Measure space complexity
        space_used = sys.getsizeof(arr)
        print(f"Space complexity: {space_used} bytes (for the stack)")

        # Measure time taken to apply HeapSort
        start_time = time.time()
        sorted_arr = heap_sort(arr)  # Use HeapSort function
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply HeapSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Push sorted elements back into the stack
        self.stack = sorted_arr

        # Output sorted stack
        for item in self.stack:
            print(f"Processing path: {item}")

# Collect all paths in the directory into a stack
def collect_paths_stack(root_directory):
    stack = Stack()
    for dirpath, dirnames, filenames in os.walk(root_directory):
        stack.push(dirpath)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            stack.push(file_path)
    return stack

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory path
stack = collect_paths_stack(root_directory)
stack.heap_sort_stack()
