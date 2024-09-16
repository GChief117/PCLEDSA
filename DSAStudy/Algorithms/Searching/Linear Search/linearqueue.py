import os
import sys
import time
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()

# Apply linear search on the queue and measure space and time complexity
def apply_linear_search_queue(root_directory, target):
    queue = Queue()

    # Step 1: Collect paths and insert into queue
    for dirpath, dirnames, filenames in os.walk(root_directory):
        queue.enqueue(dirpath)
        for filename in filenames:
            queue.enqueue(os.path.join(dirpath, filename))

    paths = list(queue.queue)

    # Measure space complexity
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes (for the queue)")

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

# Example usage for queues
root_directory = "/Volumes/CD/pCLE"
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_linear_search_queue(root_directory, target)
