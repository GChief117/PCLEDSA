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

    # QuickSort the queue
    def quicksort_queue(self):
        # Convert queue to array
        arr = list(self.queue)

        # Measure space complexity
        space_used = sys.getsizeof(self.queue)
        print(f"Space complexity: {space_used} bytes (for the queue)")

        # Measure time taken to apply QuickSort
        start_time = time.time()
        sorted_arr = quicksort(arr)  # Use QuickSort function from earlier
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply QuickSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Enqueue sorted elements back into the queue
        self.queue = deque(sorted_arr)

        # Output sorted queue
        for item in self.queue:
            print(f"Processing path: {item}")

# QuickSort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage:
queue = Queue()
queue.enqueue("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL001.txt")
queue.enqueue("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt")
queue.enqueue("/Volumes/CD/pCLE/Dye_Concentration_Experiments/CanineTissue/liver_cancer/CAN001.txt")

queue.quicksort_queue()
