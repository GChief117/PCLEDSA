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

# Binary Search Tree Node class
class BSTNode:
    def __init__(self, data, weight, value):
        self.data = data
        self.weight = weight
        self.value = value
        self.left = None
        self.right = None

# Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data, weight, value):
        new_node = BSTNode(data, weight, value)
        if not self.root:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current_node, new_node):
        if new_node.weight < current_node.weight:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_recursive(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_recursive(current_node.right, new_node)

    # In-order traversal (left, root, right)
    def in_order_traversal(self):
        weights = []
        values = []
        total_weight = 0

        def traverse(node):
            nonlocal total_weight
            if node:
                traverse(node.left)
                weights.append(node.weight)
                values.append(node.value)
                total_weight += node.weight
                traverse(node.right)

        traverse(self.root)
        return weights, values, total_weight

    # Pre-order traversal (root, left, right)
    def pre_order_traversal(self):
        weights = []
        values = []
        total_weight = 0

        def traverse(node):
            nonlocal total_weight
            if node:
                weights.append(node.weight)
                values.append(node.value)
                total_weight += node.weight
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return weights, values, total_weight

    # Post-order traversal (left, right, root)
    def post_order_traversal(self):
        weights = []
        values = []
        total_weight = 0

        def traverse(node):
            nonlocal total_weight
            if node:
                traverse(node.left)
                traverse(node.right)
                weights.append(node.weight)
                values.append(node.value)
                total_weight += node.weight

        traverse(self.root)
        return weights, values, total_weight

# Function to traverse the directory and insert into the binary search tree
def insert_in_bst(root_directory):
    bst = BinarySearchTree()

    # Start timing the traversal
    start_time = time.time()

    # Traverse the directory structure and collect file paths and sizes
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                bst.insert(file_path, file_size, file_size)  # Insert into BST based on file size (weight)
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for the BST
    space_used_bst = sys.getsizeof(bst)
    print(f"Space complexity for BST: {space_used_bst} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return bst

# Main function to run knapsack with binary search tree and dynamic capacity, including all traversals
def run_knapsack_with_dynamic_bst(root_directory):
    # Traverse the directory and insert data into the BST
    bst = insert_in_bst(root_directory)

    # In-order Traversal
    start_time = time.time()
    weights_in, values_in, capacity_in = bst.in_order_traversal()
    end_time = time.time()
    time_taken_in_order = end_time - start_time
    print(f"\nIn-order Traversal: Time taken: {time_taken_in_order:.6f} seconds")
    max_value_in_order = knapsack(values_in, weights_in, capacity_in)
    print(f"Maximum value (In-order): {max_value_in_order}")

    # Pre-order Traversal
    start_time = time.time()
    weights_pre, values_pre, capacity_pre = bst.pre_order_traversal()
    end_time = time.time()
    time_taken_pre_order = end_time - start_time
    print(f"\nPre-order Traversal: Time taken: {time_taken_pre_order:.6f} seconds")
    max_value_pre_order = knapsack(values_pre, weights_pre, capacity_pre)
    print(f"Maximum value (Pre-order): {max_value_pre_order}")

    # Post-order Traversal
    start_time = time.time()
    weights_post, values_post, capacity_post = bst.post_order_traversal()
    end_time = time.time()
    time_taken_post_order = end_time - start_time
    print(f"\nPost-order Traversal: Time taken: {time_taken_post_order:.6f} seconds")
    max_value_post_order = knapsack(values_post, weights_post, capacity_post)
    print(f"Maximum value (Post-order): {max_value_post_order}")

# Example usage for knapsack with binary search tree
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_knapsack_with_dynamic_bst(root_directory)
