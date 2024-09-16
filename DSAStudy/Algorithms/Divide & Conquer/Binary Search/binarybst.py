import os
import sys
import time

# Binary Search Tree Node class
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BSTNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self._insert_recursive(node.right, data)

    # Binary search function for the whole BST (explores all nodes)
    def binary_search_explore(self):
        # Start timing the binary search exploration
        print("\nExploring the Binary Search Tree (BST):")
        start_time = time.time()

        def explore(node):
            if node:
                print(f"Processing node with file size: {node.data} bytes")
                explore(node.left)
                explore(node.right)

        explore(self.root)

        end_time = time.time()
        print(f"Time taken for binary search exploration: {end_time - start_time:.6f} seconds")

    # In-order traversal (left, root, right)
    def in_order_traversal(self):
        def traverse(node):
            if node:
                traverse(node.left)
                print(f"In-order: {node.data} bytes")
                traverse(node.right)
        print("\nIn-order Traversal:")
        start_time = time.time()
        traverse(self.root)
        end_time = time.time()
        print(f"Time taken for in-order traversal: {end_time - start_time:.6f} seconds")

    # Pre-order traversal (root, left, right)
    def pre_order_traversal(self):
        def traverse(node):
            if node:
                print(f"Pre-order: {node.data} bytes")
                traverse(node.left)
                traverse(node.right)
        print("\nPre-order Traversal:")
        start_time = time.time()
        traverse(self.root)
        end_time = time.time()
        print(f"Time taken for pre-order traversal: {end_time - start_time:.6f} seconds")

    # Post-order traversal (left, right, root)
    def post_order_traversal(self):
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                print(f"Post-order: {node.data} bytes")
        print("\nPost-order Traversal:")
        start_time = time.time()
        traverse(self.root)
        end_time = time.time()
        print(f"Time taken for post-order traversal: {end_time - start_time:.6f} seconds")

# Function to traverse the directory and insert file sizes into a BST
def traverse_directory_for_bst(root_directory):
    bst = BinarySearchTree()

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                bst.insert(file_size)
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for the BST
    space_used_bst = sys.getsizeof(bst)
    print(f"Space complexity for BST: {space_used_bst} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return bst

# Main function to perform binary search exploration and all traversals with a BST
def run_binary_search_with_bst(root_directory):
    # Traverse the directory and insert file sizes into a BST
    bst = traverse_directory_for_bst(root_directory)

    # Perform binary search exploration across all nodes
    bst.binary_search_explore()

    # Perform in-order, pre-order, and post-order traversals
    bst.in_order_traversal()
    bst.pre_order_traversal()
    bst.post_order_traversal()

# Example usage for binary search with BST
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_binary_search_with_bst(root_directory)
