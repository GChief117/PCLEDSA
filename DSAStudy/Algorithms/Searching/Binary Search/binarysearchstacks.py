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

    # Apply binary search on stack data (sorted)
    def binary_search_stack(self, target):
        self.stack.sort()  # Sort the stack data for binary search
        low, high = 0, len(self.stack) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.stack[mid] == target:
                return mid
            elif self.stack[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# Apply binary search on the stack and measure space and time complexity
def apply_binary_search_stack(root_directory, target):
    stack = Stack()

    # Step 1: Collect paths and insert into stack
    for dirpath, dirnames, filenames in os.walk(root_directory):
        stack.push(dirpath)
        for filename in filenames:
            stack.push(os.path.join(dirpath, filename))

    # Step 2: Apply binary search
    index = stack.binary_search_stack(target)

    # Measure space complexity
    space_used = sys.getsizeof(stack.stack)
    print(f"Space complexity: {space_used} bytes (for the stack)")

    # Measure time complexity
    start_time = time.time()
    index = stack.binary_search_stack(target)
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to perform binary search: {time_taken:.6f} seconds")
    print(f"Time complexity: O(log n)")

    if index != -1:
        print(f"Target found at index {index}")
    else:
        print("Target not found")

# Example usage for stacks
root_directory = "/Volumes/CD/pCLE"
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_binary_search_stack(root_directory, target)
