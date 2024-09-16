import os
import time
import sys
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None

    # HeapSort the queue
    def heap_sort_queue(self):
        # Convert queue to array
        arr = list(self.queue)

        # Measure space complexity
        space_used = sys.getsizeof(arr)
        print(f"Space complexity: {space_used} bytes (for the queue)")

        # Measure time taken to apply HeapSort
        start_time = time.time()
        sorted_arr = heap_sort(arr)  # Use HeapSort function
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply HeapSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Re-enqueue sorted elements
        self.queue = deque(sorted_arr)

        # Output sorted queue
        for item in self.queue:
            print(f"Processing path: {item}")

# Collect all paths in the directory into a queue
def collect_paths_queue(root_directory):
    queue = Queue()
    for dirpath, dirnames, filenames in os.walk(root_directory):
        queue.enqueue(dirpath)
        for filename in filenames:
            queue.enqueue(os.path.join(dirpath, filename))
    return queue

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory path
queue = collect_paths_queue(root_directory)
queue.heap_sort_queue()
