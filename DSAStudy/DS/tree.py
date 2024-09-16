import os
import time
import sys

# Binary Search Tree (BST) implementation for storing paths
class BST:
    class Node:
        def __init__(self, data):
            self.data = data  # Store the path in the node
            self.left = None  # Left child
            self.right = None  # Right child

    def __init__(self):
        self.root = None  # Initialize the root of the tree

    # Insert a new path into the BST
    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)  # Create the root node
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        # Compare the path lexicographically
        if data < node.data:
            if node.left is None:
                node.left = self.Node(data)  # Insert as the left child
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = self.Node(data)  # Insert as the right child
            else:
                self._insert_recursive(node.right, data)

    # In-order traversal of the BST (left -> root -> right)
    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(f"Processing path: {node.data}")  # Simulate processing
            self.in_order_traversal(node.right)

# Collect all paths in the directory into a BST
def collect_paths_into_bst(root_directory):
    bst = BST()
    
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Insert directory path into the BST
        bst.insert(dirpath)
        
        # Insert each file path in the directory into the BST
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            bst.insert(file_path)
    
    return bst

# Function to perform operations and measure time and space complexity
def perform_operations_on_bst(bst):
    # Measure space complexity
    space_used = sys.getsizeof(bst)
    print(f"Space complexity: {space_used} bytes (for the binary search tree)")

    # Time complexity: Measure time to traverse the entire BST (in-order traversal)
    start_time = time.time()
    bst.in_order_traversal(bst.root)  # Traverse and apply operations
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to traverse the BST: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n), where n is the number of elements (paths)")

# Main function
def main():
    # Define the root directory (adjust this to your actual directory path)
    root_directory = "/Volumes/CD/pCLE"
    
    # Step 1: Collect all paths into the BST
    bst = collect_paths_into_bst(root_directory)
    
    # Step 2: Perform operations on the BST and measure complexities
    perform_operations_on_bst(bst)

# Run the main function
if __name__ == "__main__":
    main()
