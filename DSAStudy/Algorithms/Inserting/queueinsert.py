import sys
import time
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        start_time = time.time()  # Start the timer
        self.queue.append(data)
        end_time = time.time()  # End the timer

        # Measure space complexity
        space_used = sys.getsizeof(self.queue)
        print(f"Space complexity: {space_used} bytes (for the queue)")

        # Measure time complexity
        time_taken = end_time - start_time
        print(f"Time taken to enqueue into queue: {time_taken:.6f} seconds")
        print(f"Time complexity: O(1)")

    def display(self):
        for item in self.queue:
            print(f"Queue path: {item}")

# Example usage for the queue
queue = Queue()
queue.enqueue("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL001.txt")
queue.enqueue("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt")
queue.enqueue("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL003.txt")
queue.display()
