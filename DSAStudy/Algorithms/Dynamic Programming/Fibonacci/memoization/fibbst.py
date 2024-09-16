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

    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.data)
            self.in_order_traversal(node.right, result)
        return result

# Insert directories into a BST and calculate Fibonacci during the insertion
def insert_in_bst_fib(root_directory):
    bst = BST()
    memo = {}

    for dirpath, dirnames, filenames in os.walk(root_directory):
        bst.insert(dirpath)  # Insert directory path into the BST
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            bst.insert(file_path)  # Insert file path into the BST

            # Calculate Fibonacci for the current path length using memoization
            fib_result = fibonacci_memo(len(file_path), memo)
            print(f"Fibonacci({len(file_path)}) result for file: {file_path} = {fib_result}")

    # Perform in-order traversal
    in_order_paths = bst.in_order_traversal(bst.root)
    print("\n--- In-order Traversal Results ---")
    for path in in_order_paths:
        print(f"Path: {path}")

    # Measure space complexity (space used by the BST)
    space_used = sys.getsizeof(bst)
    print(f"Space complexity: {space_used} bytes (for the BST)")

    # Measure time complexity for traversal
    start_time = time.time()
    bst.in_order_traversal(bst.root)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken for in-order traversal: {time_taken:.6f} seconds")

# Example usage for the BST
insert_in_bst_fib(root_directory)
