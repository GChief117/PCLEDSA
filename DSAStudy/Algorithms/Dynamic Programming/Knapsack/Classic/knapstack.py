import os
import sys
import time

# Knapsack dynamic programming function
def knapsack(values, weights, capacity):
    n = len(values)
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Start timing the knapsack computation
    start_time = time.time()

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp_table[i][w] = max(values[i - 1] + dp_table[i - 1][w - weights[i - 1]], dp_table[i - 1][w])
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    end_time = time.time()
    time_taken = end_time - start_time

    # Output time complexity
    print(f"Time taken to compute knapsack: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n * W), where n = {n}, W = {capacity}")

    # Measure space complexity
    space_used = sys.getsizeof(dp_table)
    print(f"Space complexity: {space_used} bytes for the dp table")

    # The last entry contains the maximum value we can achieve
    return dp_table[n][capacity]

# Stack class
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data, weight, value):
        self.stack.append((data, weight, value))

    def get_weights_and_values(self):
        weights = []
        values = []
        total_capacity = 0
        for item in self.stack:
            weights.append(item[1])  # Weight
            values.append(item[2])  # Value
            total_capacity += item[1]
        return weights, values, total_capacity

# Function to traverse the directory and insert into a stack
def insert_in_stack(root_directory):
    stack = Stack()
    total_capacity = 0

    # Start timing the traversal
    start_time = time.time()

    # Traverse the directory and collect file paths and sizes
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                stack.push(file_path, file_size, file_size)  # Push to stack
                total_capacity += file_size  # Dynamically calculate total capacity
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for stack
    space_used_stack = sys.getsizeof(stack.stack)
    print(f"Space complexity for stack: {space_used_stack} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return stack, total_capacity

# Main function to run knapsack with stack and dynamic capacity
def run_knapsack_with_dynamic_stack(root_directory):
    # Traverse the directory and insert data into the stack
    stack, total_capacity = insert_in_stack(root_directory)

    # Retrieve weights and values from the stack
    weights, values, dynamic_capacity = stack.get_weights_and_values()

    # Apply the knapsack algorithm with the dynamically calculated total capacity
    max_value = knapsack(values, weights, dynamic_capacity)
    print(f"Maximum value achievable without exceeding dynamic capacity: {max_value}")

# Example usage for knapsack with stack
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_knapsack_with_dynamic_stack(root_directory)
