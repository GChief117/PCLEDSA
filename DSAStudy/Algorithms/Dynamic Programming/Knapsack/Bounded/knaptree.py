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

# Tree node class
class TreeNode:
    def __init__(self, data, weight, value, count):
        self.data = data
        self.weight = weight
        self.value = value
        self.count = count  # Bounded constraint (number of copies)
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Tree class
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data, weight, value, count, parent=None):
        new_node = TreeNode(data, weight, value, count)
        if self.root is None:
            self.root = new_node
        elif parent:
            parent.add_child(new_node)
        return new_node

    def traverse_tree(self):
        weights = []
        values = []
        counts = []
        total_weight = 0

        def traverse(node):
            nonlocal total_weight
            if node:
                weights.append(node.weight)
                values.append(node.value)
                counts.append(node.count)
                total_weight += node.weight
                for child in node.children:
                    traverse(child)

        traverse(self.root)
        return weights, values, counts, total_weight

# Function to traverse the directory and insert into a tree
def insert_in_tree_bounded(root_directory):
    tree = Tree()

    # Start timing the traversal
    start_time = time.time()

    # Traverse the directory structure and collect file paths and sizes
    parent_map = {}  # To keep track of parent-child relationships in the tree
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if tree.root is None:
            parent_map[dirpath] = tree.insert(dirpath, len(dirpath), len(dirpath), 1)  # Root node

        # Add subdirectories as children
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            subdir_node = tree.insert(subdir_path, len(subdir_path), len(subdir_path), 1, parent_map[dirpath])
            parent_map[subdir_path] = subdir_node

        # Add files as children
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                file_node = tree.insert(file_path, file_size, file_size, 3, parent_map[dirpath])  # 3 copies per file
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for the tree
    space_used_tree = sys.getsizeof(tree)
    print(f"Space complexity for tree: {space_used_tree} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return tree

# Main function to run bounded knapsack with tree and dynamic capacity
def run_bounded_knapsack_with_tree(root_directory):
    # Traverse the directory and insert data into the tree
    tree = insert_in_tree_bounded(root_directory)

    # Retrieve weights, values, and counts from the tree
    weights, values, counts, total_capacity = tree.traverse_tree()

    # Apply the bounded knapsack algorithm with the dynamically calculated total capacity
    max_value = bounded_knapsack(values, weights, counts, total_capacity)
    print(f"Maximum value achievable with bounded knapsack: {max_value}")

# Example usage
