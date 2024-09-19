import os
import time
import sys

# Stack implementation for storing paths
class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to store stack elements (paths)

    # Push a new path onto the stack
    def push(self, data):
        self.stack.append(data)  # Add a path to the top of the stack

    # Pop a path off the stack (LIFO)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the top path from the stack
        return None

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Traverse the stack (process each path from top to bottom)
    def traverse_and_apply_operations(self):
        while not self.is_empty():
            path = self.pop()  # Pop the top path from the stack
            # Simulate an operation (you can apply real algorithms here)
            # print(f"Processing path: {path}")  # Uncomment to print paths if needed

# Collect all paths in the directory into a stack
def collect_paths_into_stack(root_directory):
    stack = Stack()
    
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Push directory path onto the stack
        stack.push(dirpath)
        
        # Push each file path in the directory onto the stack
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            stack.push(file_path)
    
    return stack

# Function to perform operations and measure time and space complexity
def perform_operations_on_stack(stack):
    # Measure space complexity (size of the stack + size of each path in the stack)
    space_used = sys.getsizeof(stack.stack) + sum([sys.getsizeof(path) for path in stack.stack])
    
    # Time complexity: Measure time to traverse the entire stack
    start_time = time.time()
    stack.traverse_and_apply_operations()  # Traverse and apply operations
    end_time = time.time()

    time_taken = end_time - start_time
    
    # Output the results for Excel
    print(f"Directory Traversal, O(n), O(n), {time_taken:.6f} seconds, {space_used} bytes")

# Main function
def main():
    # Define the root directory (adjust this to your actual directory path)
    root_directory = "/Volumes/CD/pCLE"
    
    # Step 1: Collect all paths into the stack
    stack = collect_paths_into_stack(root_directory)
    
    # Step 2: Perform operations on the stack and measure complexities
    perform_operations_on_stack(stack)

# Run the main function
if __name__ == "__main__":
    main()
