import os
import sys
import time
from collections import deque

# Queue class using deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def to_list(self):
        return list(self.queue)

# Karatsuba multiplication function
def karatsuba(x, y):
    # Start timing the Karatsuba multiplication
    start_time = time.time()

    if x < 10 or y < 10:
        result = x * y
    else:
        m = min(len(str(x)), len(str(y)))
        m2 = m // 2

        high1, low1 = divmod(x, 10**m2)
        high2, low2 = divmod(y, 10**m2)

        z0 = karatsuba(low1, low2)
        z1 = karatsuba((low1 + high1), (low2 + high2))
        z2 = karatsuba(high1, high2)

        result = (z2 * 10**(2 * m2)) + ((z1 - z2 - z0) * 10**m2) + z0

    end_time = time.time()
    print(f"Time taken for Karatsuba multiplication: {end_time - start_time:.6f} seconds")
    print(f"Time complexity: O(n^1.585)")
    return result

# Function to traverse the directory and collect file sizes using a queue
def traverse_directory_for_queue(root_directory):
    queue = Queue()

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                queue.enqueue(file_size)
            except OSError:
                continue

    end_time = time.time()
    print(f"Time taken for directory traversal: {end_time - start_time:.6f} seconds")

    # Measure space complexity for queue
    space_used_queue = sys.getsizeof(queue)
    print(f"Space complexity for queue: {space_used_queue} bytes")

    return queue

# Main function for Karatsuba algorithm with queue
def run_karatsuba_with_queue(root_directory):
    # Traverse the directory and collect file sizes
    queue = traverse_directory_for_queue(root_directory)
    file_sizes = queue.to_list()

    # Select two largest file sizes for Karatsuba multiplication
    if len(file_sizes) >= 2:
        x, y = sorted(file_sizes)[-2:]
        print(f"Multiplying {x} and {y} using Karatsuba Algorithm")
        result = karatsuba(x, y)
        print(f"Result of Karatsuba multiplication: {result}")
    else:
        print("Not enough files to perform Karatsuba multiplication")

# Example usage for Karatsuba algorithm with queue
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_karatsuba_with_queue(root_directory)
