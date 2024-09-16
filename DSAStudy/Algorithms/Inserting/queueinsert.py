import os
import sys
import time
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, file_path, file_size):
        self.queue.append((file_path, file_size))

# Function to insert a file into a queue (simulating file insertion)
def insert_file_into_queue(queue, file_path):
    try:
        file_size = os.path.getsize(file_path)
    except OSError:
        print(f"Error retrieving file size for {file_path}")
        return
    
    # Start timing the insertion
    start_time = time.time()

    queue.enqueue(file_path, file_size)

    end_time = time.time()
    print(f"Time taken for queue file insertion: {end_time - start_time:.6f} seconds")
    print(f"Time complexity: O(1)")

# Function to traverse the directory and collect files using queue
def traverse_directory_for_queue(root_directory):
    queue = Queue()

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                queue.enqueue(file_path, file_size)
            except OSError:
                continue

    end_time = time.time()
    print(f"Time taken for directory traversal: {end_time - start_time:.6f} seconds")

    # Measure space complexity for queue
    space_used_queue = sys.getsizeof(queue)
    print(f"Space complexity for queue: {space_used_queue} bytes")

    return queue

# Main function to perform file insertion into queue
def run_file_insertion_with_queue(root_directory, file_to_insert):
    # Traverse the directory and collect files
    queue = traverse_directory_for_queue(root_directory)

    # Insert the new file into the queue
    print(f"\nInserting {file_to_insert} into the queue:")
    insert_file_into_queue(queue, file_to_insert)

# Example usage for queue file insertion
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    file_to_insert = "/path/to/new/file.txt"  # Replace with the path of the new file
    run_file_insertion_with_queue(root_directory, file_to_insert)
