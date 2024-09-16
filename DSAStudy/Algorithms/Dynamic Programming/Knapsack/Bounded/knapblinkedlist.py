import os
import sys
import time

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

# Linked list node class
class Node:
    def __init__(self, data, weight, value, count):
        self.data = data
        self.weight = weight
        self.value = value
        self.count = count  # Bounded constraint (number of copies)
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, weight, value, count):
        new_node = Node(data, weight, value, count)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def traverse(self):
        current = self.head
        weights = []
        values = []
        counts = []
        total_capacity = 0
        while current:
            weights.append(current.weight)
            values.append(current.value)
            counts.append(current.count)
            total_capacity += current.weight
            current = current.next
        return weights, values, counts, total_capacity

# Function to traverse the directory and insert into the linked list
def insert_in_linked_list_bounded(root_directory):
    linked_list = LinkedList()
    total_capacity = 0

    # Start timing the traversal
    start_time = time.time()

    # Traverse the directory and collect file paths and sizes
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                linked_list.insert(file_path, file_size, file_size, 3)  # Example: allow 3 copies of each file
                total_capacity += file_size  # Dynamically calculate total capacity
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for the linked list
    space_used_list = sys.getsizeof(linked_list)
    print(f"Space complexity for linked list: {space_used_list} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return linked_list

# Main function to run the bounded knapsack problem using linked list with dynamic capacity
def run_bounded_knapsack_with_linked_list(root_directory):
    # Traverse the directory and insert data into the linked list
    linked_list = insert_in_linked_list_bounded(root_directory)

    # Retrieve weights, values, and counts from the linked list
    weights, values, counts, total_capacity = linked_list.traverse()

    # Apply the bounded knapsack algorithm with the dynamically calculated total capacity
    max_value = bounded_knapsack(values, weights, counts, total_capacity)
    print(f"Maximum value achievable with bounded knapsack: {max_value}")

# Example usage for bounded knapsack with linked list
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_bounded_knapsack_with_linked_list(root_directory)
