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

    # MergeSort the queue
    def merge_sort_queue(self):
        # Convert queue to array
        arr = list(self.queue)

        # Measure space complexity
        space_used = sys.getsizeof(self.queue)
        print(f"Space complexity: {space_used} bytes (for the queue)")

        # Measure time taken to apply MergeSort
        start_time = time.time()
        sorted_arr = merge_sort(arr)  # Use MergeSort function
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply MergeSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Enqueue sorted elements back into the queue
        self.queue = deque(sorted_arr)

        # Output sorted queue
        for item in self.queue:
            print(f"Processing path: {item}")

# MergeSort function for array
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Merge function to merge two sorted subarrays
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Collect all paths in the directory into a queue
def collect_paths_queue(root_directory):
    queue = Queue()
    for dirpath, dirnames, filenames in os.walk(root_directory):
        queue.enqueue(dirpath)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            queue.enqueue(file_path)
    return queue

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory path
queue = collect_paths_queue(root_directory)
queue.merge_sort_queue()
