import os
import sys
import time

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, file_path, file_size):
        self.stack.append((file_path, file_size))

# Function to insert a file into a stack (simulating file insertion)
def insert_file_into_stack(stack, file_path):
    try:
        file_size = os.path.getsize(file_path)
    except OSError:
        print(f"Error retrieving file size for {file_path}")
        return
    
    # Start timing the insertion
    start_time = time.time()

    stack.push(file_path, file_size)

    end_time = time.time()
    print(f"Time taken for stack file insertion: {end_time - start_time:.6f} seconds")
    print(f"Time complexity: O(1)")

# Function to traverse the directory and collect files using stack
def traverse_directory_for_stack(root_directory):
    stack = Stack()

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                stack.push(file_path, file_size)
            except OSError:
                continue

    end_time = time.time()
    print(f"Time taken for directory traversal: {end_time - start_time:.6f} seconds")

    # Measure space complexity for stack
    space_used_stack = sys.getsizeof(stack)
    print(f"Space complexity for stack: {space_used_stack} bytes")

    return stack

# Main function to perform file insertion into stack
def run_file_insertion_with_stack(root_directory, file_to_insert):
    # Traverse the directory and collect files
    stack = traverse_directory_for_stack(root_directory)

    # Insert the new file into the stack
    print(f"\nInserting {file_to_insert} into the stack:")
    insert_file_into_stack(stack, file_to_insert)

# Example usage for stack file insertion
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    file_to_insert = "/path/to/new/file.txt"  # Replace with the path of the new file
    run_file_insertion_with_stack(root_directory, file_to_insert)
