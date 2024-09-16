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

# Tree node class
class TreeNode:
    def __init__(self, data, weight, value):
        self.data = data
        self.weight = weight
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Tree class
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data, weight, value, parent=None):
        new_node = TreeNode(data, weight, value)
        if self.root is None:
            self.root = new_node
        elif parent:
            parent.add_child(new_node)
        return new_node

    def traverse_tree(self):
        total_weight = 0
        total_value = 0
        weights = []
        values = []

        def traverse_node(node):
            nonlocal total_weight, total_value
            if node:
                weights.append(node.weight)
                values.append(node.value)
                total_weight += node.weight
                total_value += node.value
                for child in node.children:
                    traverse_node(child)

        traverse_node(self.root)
        return weights, values, total_weight

# Function to traverse the directory and insert into a tree
def insert_in_tree(root_directory):
    tree = Tree()

    # Start timing the traversal
    start_time = time.time()

    # Traverse the directory structure and collect file paths and sizes
    parent_map = {}  # To keep track of parent-child relationships in the tree
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if tree.root is None:
            parent_map[dirpath] = tree.insert(dirpath, len(dirpath), len(dirpath))  # Root node
        else:
            parent = parent_map[dirpath]

            # Add subdirectories as children
            for dirname in dirnames:
                subdir_path = os.path.join(dirpath, dirname)
                subdir_node = tree.insert(subdir_path, len(subdir_path), len(subdir_path), parent)
                parent_map[subdir_path] = subdir_node

            # Add files as children
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                try:
                    file_size = os.path.getsize(file_path)
                    tree.insert(file_path, file_size, file_size, parent)
                except OSError:
                    continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for the tree
    space_used_tree = sys.getsizeof(tree)
    print(f"Space complexity for tree: {space_used_tree} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return tree

# Main function to run knapsack with tree and dynamic capacity
def run_knapsack_with_dynamic_tree(root_directory):
    # Traverse the directory and insert data into the tree
    tree = insert_in_tree(root_directory)

    # Retrieve weights and values from the tree
    weights, values, dynamic_capacity = tree.traverse_tree()

    # Apply the knapsack algorithm with the dynamically calculated total capacity
    max_value = knapsack(values, weights, dynamic_capacity)
    print(f"Maximum value achievable without exceeding dynamic capacity: {max_value}")

# Example usage for knapsack with tree
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_knapsack_with_dynamic_tree(root_directory)
