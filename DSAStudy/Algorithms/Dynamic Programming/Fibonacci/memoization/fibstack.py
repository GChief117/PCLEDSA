import os
import sys
import time

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

# Insert directories into a stack while calculating Fibonacci for each path
def insert_in_stack_fib(root_directory):
    stack = Stack()
    memo = {}

    for dirpath, dirnames, filenames in os.walk(root_directory):
        stack.push(dirpath)  # Insert directory path into the stack
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            stack.push(file_path)  # Insert file path into the stack

            # Calculate Fibonacci for the current path length using memoization
            fib_result = fibonacci_memo(len(file_path), memo)
            print(f"Fibonacci({len(file_path)}) result for file: {file_path} = {fib_result}")

    # Measure space complexity (space used by the stack)
    space_used = sys.getsizeof(stack.stack)
    print(f"Space complexity: {space_used} bytes (for the stack)")

    # Measure time complexity
    start_time = time.time()
    while stack.stack:
        fibonacci_memo(len(stack.stack.pop()), memo)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to process stack: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n)")

# Example usage for the stack
insert_in_stack_fib(root_directory)
