import os
import sys
import time

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

# Insert directories and files into a stack while calculating Fibonacci using tabulation
def insert_in_stack_fib_tab(root_directory):
    stack = Stack()

    # Traverse the directory structure
    for dirpath, dirnames, filenames in os.walk(root_directory):
        stack.push(dirpath)  # Insert directory path into the stack
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            stack.push(file_path)  # Insert file path into the stack

            # Calculate Fibonacci for the current path length using tabulation
            fib_result = fibonacci_tab(len(file_path))
            print(f"Fibonacci({len(file_path)}) result for file: {file_path} = {fib_result}")

    # Measure space complexity (space used by the stack)
    space_used = sys.getsizeof(stack.stack)
    print(f"Space complexity: {space_used} bytes (for the stack)")

    # Measure time complexity
    start_time = time.time()
    while stack.stack:
        fibonacci_tab(len(stack.stack.pop()))
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to process stack: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n)")

# Example usage for the stack with tabulation
root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
insert_in_array_fib_tab(root_directory)
