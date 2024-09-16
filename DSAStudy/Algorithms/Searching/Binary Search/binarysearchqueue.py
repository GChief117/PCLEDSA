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

    def binary_search_queue(self, target):
        arr = list(self.queue)  # Convert to array for sorting and binary search
        arr.sort()
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# Apply binary search on the queue and measure space and time complexity
def apply_binary_search_queue(root_directory, target):
    queue = Queue()

    # Step 1: Collect paths and insert into queue
    for dirpath, dirnames, filenames in os.walk(root_directory):
        queue.enqueue(dirpath)
        for filename in filenames:
            queue.enqueue(os.path.join(dirpath, filename))

    # Step 2: Apply binary search
    index = queue.binary_search_queue(target)

    # Measure space complexity
    space_used = sys.getsizeof(list(queue.queue))
    print(f"Space complexity: {space_used} bytes (for the queue)")

    # Measure time complexity
    start_time = time.time()
    index = queue.binary_search_queue(target)
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to perform binary search: {time_taken:.6f} seconds")
    print(f"Time complexity: O(log n)")

    if index != -1:
        print(f"Target found at index {index}")
    else:
        print("Target not found")

# Example usage for queues
root_directory = "/Volumes/CD/pCLE"
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_binary_search_queue(root_directory, target)
