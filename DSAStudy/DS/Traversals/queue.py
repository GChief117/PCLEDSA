import os
import time
import sys
from collections import deque

# Queue implementation for storing paths
class Queue:
    def __init__(self):
        self.queue = deque()  # Initialize a deque as a queue

    # Enqueue a new path into the queue (add to the back of the queue)
    def enqueue(self, data):
        self.queue.append(data)  # Add path to the end of the queue

    # Dequeue a path from the queue (remove from the front of the queue)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()  # Remove and return the front path
        return None

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Traverse the queue (process each path from front to back)
    def traverse_and_apply_operations(self):
        while not self.is_empty():
            path = self.dequeue()  # Dequeue the front path
            # Simulate an operation (you can apply real algorithms here)
            # print(f"Processing path: {path}")  # Uncomment to print the path if needed

# Collect all paths in the directory into a queue
def collect_paths_into_queue(root_directory):
    queue = Queue()
    
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Enqueue directory path into the queue
        queue.enqueue(dirpath)
        
        # Enqueue each file path in the directory into the queue
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            queue.enqueue(file_path)
    
    return queue

# Function to perform operations and measure time and space complexity
def perform_operations_on_queue(queue):
    # Measure space complexity (size of the queue + size of each path in the queue)
    space_used = sys.getsizeof(queue.queue) + sum([sys.getsizeof(path) for path in queue.queue])
    
    # Time complexity: Measure time to traverse the entire queue
    start_time = time.time()
    queue.traverse_and_apply_operations()  # Traverse and apply operations
    end_time = time.time()

    time_taken = end_time - start_time
    
    # Output the results for Excel
    print(f"Directory Traversal, O(n), O(n), {time_taken:.6f} seconds, {space_used} bytes")

# Main function
def main():
    # Define the root directory (adjust this to your actual directory path)
    root_directory = "/Volumes/CD/pCLE"
    
    # Step 1: Collect all paths into the queue
    queue = collect_paths_into_queue(root_directory)
    
    # Step 2: Perform operations on the queue and measure complexities
    perform_operations_on_queue(queue)

# Run the main function
if __name__ == "__main__":
    main()
