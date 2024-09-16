import os
import sys
import time
from collections import deque

# Bounded Knapsack dynamic programming function
def bounded_knapsack(values, weights, counts, capacity):
    n = len(values)
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Start timing the knapsack computation
    start_time = time.time()

    # Build the table considering bounded counts for each item
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            for k in range(counts[i - 1] + 1):  # Check k copies of the item
                if k * weights[i - 1] <= w:
                    dp_table[i][w] = max(dp_table[i][w], dp_table[i - 1][w - k * weights[i - 1]] + k * values[i - 1])

    end_time = time.time()
    time_taken = end_time - start_time

    # Output time complexity
    print(f"Time taken to compute bounded knapsack: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n * W * c), where n = {n}, W = {capacity}, c = counts")

    # Measure space complexity
    space_used = sys.getsizeof(dp_table)
    print(f"Space complexity: {space_used} bytes for the dp table")

    # The last entry contains the maximum value we can achieve
    return dp_table[n][capacity]

# Queue class using deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data, weight, value, count):
        self.queue.append((data, weight, value, count))  # Store file path, weight, value, and count

    def get_weights_and_values(self):
        weights = []
        values = []
        counts = []
        total_capacity = 0
        for item in self.queue:
            weights.append(item[1])  # Weight
            values.append(item[2])  # Value
            counts.append(item[3])  # Count (number of copies allowed)
            total_capacity += item[1]
        return weights, values, counts, total_capacity

# Function to traverse the directory and insert into a queue
def insert_in_queue_bounded(root_directory):
    queue = Queue()
    total_capacity = 0

    # Start timing the traversal
    start_time = time.time()

    # Traverse the directory and collect file paths and sizes
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                queue.enqueue(file_path, file_size, file_size, 3)  # Example: allow 3 copies of each file
                total_capacity += file_size  # Dynamically calculate total capacity
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for the queue
    space_used_queue = sys.getsizeof(queue.queue)
    print(f"Space complexity for queue: {space_used_queue} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return queue

# Main function to run the bounded knapsack problem using queue with dynamic capacity
def run_bounded_knapsack_with_queue(root_directory):
    # Traverse the directory and insert data into the queue
    queue = insert_in_queue_bounded(root_directory)

    # Retrieve weights, values, and counts from the queue
    weights, values, counts, total_capacity = queue.get_weights_and_values()

    # Apply the bounded knapsack algorithm with the dynamically calculated total capacity
    max_value = bounded_knapsack(values, weights, counts, total_capacity)
    print(f"Maximum value achievable with bounded knapsack: {max_value}")

# Example usage for bounded knapsack with queue
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_bounded_knapsack_with_queue(root_directory)
