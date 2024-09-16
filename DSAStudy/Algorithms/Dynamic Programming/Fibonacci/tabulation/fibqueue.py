import os
import sys
import time
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

# Insert directories and files into a queue while calculating Fibonacci using tabulation
def insert_in_queue_fib_tab(root_directory):
    queue = Queue()

    # Traverse the directory structure
    for dirpath, dirnames, filenames in os.walk(root_directory):
        queue.enqueue(dirpath)  # Insert directory path into the queue
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            queue.enqueue(file_path)  # Insert file path into the queue

            # Calculate Fibonacci for the current path length using tabulation
            fib_result = fibonacci_tab(len(file_path))
            print(f"Fibonacci({len(file_path)}) result for file: {file_path} = {fib_result}")

    # Measure space complexity (space used by the queue)
    space_used = sys.getsizeof(queue.queue)
    print(f"Space complexity: {space_used} bytes (for the queue)")

    # Measure time complexity
    start_time = time.time()
    while queue.queue:
        fibonacci_tab(len(queue.queue.popleft()))
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to process queue: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n)")

# Example usage for the queue with tabulation
root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
insert_in_array_fib_tab(root_directory)
