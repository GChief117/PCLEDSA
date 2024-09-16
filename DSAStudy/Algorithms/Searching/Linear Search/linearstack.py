import os
import sys
import time

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self):
        return self.stack[-1] if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0

# Apply linear search on the stack and measure space and time complexity
def apply_linear_search_stack(root_directory, target):
    stack = Stack()

    # Step 1: Collect paths and insert into stack
    for dirpath, dirnames, filenames in os.walk(root_directory):
        stack.push(dirpath)
        for filename in filenames:
            stack.push(os.path.join(dirpath, filename))

    paths = stack.stack

    # Measure space complexity
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes (for the stack)")

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

# Example usage for stacks
root_directory = "/Volumes/CD/pCLE"
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_linear_search_stack(root_directory, target)
