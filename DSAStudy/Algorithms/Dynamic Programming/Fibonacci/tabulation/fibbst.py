import os
import sys
import time

class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Insert a new node into the BST
    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = self.Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = self.Node(data)
            else:
                self._insert_recursive(node.right, data)

    # In-order traversal: Left -> Node -> Right
    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.data)
            self.in_order_traversal(node.right, result)
        return result

    # Pre-order traversal: Node -> Left -> Right
    def pre_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.data)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    # Post-order traversal: Left -> Right -> Node
    def post_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.data)
        return result

# Fibonacci tabulation function
def fibonacci_tab(n):
    if n <= 1:
        return n

    fib_table = [0] * (n + 1)
    fib_table[1] = 1

    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]

# Insert directories and files into a BST and calculate Fibonacci using tabulation
def insert_in_bst_fib_tab(root_directory):
    bst = BST()

    # Traverse the directory structure
    for dirpath, dirnames, filenames in os.walk(root_directory):
        bst.insert(dirpath)  # Insert directory path into the BST
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            bst.insert(file_path)  # Insert file path into the BST

            # Calculate Fibonacci for the file path length using tabulation
            fib_result = fibonacci_tab(len(file_path))
            print(f"Fibonacci({len(file_path)}) result for file: {file_path} = {fib_result}")

    # Perform all traversals
    print("\n--- In-order Traversal ---")
    in_order_paths = bst.in_order_traversal(bst.root)
    for path in in_order_paths:
        print(f"Path: {path}")

    print("\n--- Pre-order Traversal ---")
    pre_order_paths = bst.pre_order_traversal(bst.root)
    for path in pre_order_paths:
        print(f"Path: {path}")

    print("\n--- Post-order Traversal ---")
    post_order_paths = bst.post_order_traversal(bst.root)
    for path in post_order_paths:
        print(f"Path: {path}")

    # Measure space complexity (space used by the BST)
    space_used = sys.getsizeof(bst)
    print(f"\nSpace complexity: {space_used} bytes (for the BST)")

    # Measure time complexity for traversal
    start_time = time.time()
    bst.in_order_traversal(bst.root)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken for in-order traversal: {time_taken:.6f} seconds")

# Example usage for the BST with all traversals
root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
insert_in_bst_fib_tab(root_directory)
