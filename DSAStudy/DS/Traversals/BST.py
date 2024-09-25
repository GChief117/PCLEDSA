import os
import time
import sys
from collections import deque

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
            self.in_order_traversal(node.right)

    # Pre-order traversal of the BST (root -> left -> right)
    def pre_order_traversal(self, node):
        if node is not None:
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    # Post-order traversal of the BST (left -> right -> root)
    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)

    # Breadth-First Search (BFS)
    def bfs(self):
        if self.root is None:
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    # Depth-First Search (DFS) using pre-order traversal
    def dfs(self, node):
        if node is not None:
            self.dfs(node.left)
            self.dfs(node.right)

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
    
    # Store results for formatted output
    results = []

    # In-order traversal
    start_time = time.time()
    bst.in_order_traversal(bst.root)
    end_time = time.time()
    time_taken_in_order = end_time - start_time
    results.append(["In-order Traversal", "O(n)", "O(n)", f"{time_taken_in_order:.6f} seconds", f"{space_used} bytes"])

    # Pre-order traversal
    start_time = time.time()
    bst.pre_order_traversal(bst.root)
    end_time = time.time()
    time_taken_pre_order = end_time - start_time
    results.append(["Pre-order Traversal", "O(n)", "O(n)", f"{time_taken_pre_order:.6f} seconds", f"{space_used} bytes"])

    # Post-order traversal
    start_time = time.time()
    bst.post_order_traversal(bst.root)
    end_time = time.time()
    time_taken_post_order = end_time - start_time
    results.append(["Post-order Traversal", "O(n)", "O(n)", f"{time_taken_post_order:.6f} seconds", f"{space_used} bytes"])

    # Breadth-First Search (BFS)
    start_time = time.time()
    bst.bfs()
    end_time = time.time()
    time_taken_bfs = end_time - start_time
    results.append(["BFS Traversal", "O(n)", "O(n)", f"{time_taken_bfs:.6f} seconds", f"{space_used} bytes"])

    # Depth-First Search (DFS)
    start_time = time.time()
    bst.dfs(bst.root)
    end_time = time.time()
    time_taken_dfs = end_time - start_time
    results.append(["DFS Traversal", "O(n)", "O(n)", f"{time_taken_dfs:.6f} seconds", f"{space_used} bytes"])

    # Print the results in the desired format
    print(f"{'Operation':<25} {'Time Complexity':<15} {'Space Complexity':<15} {'Time (in seconds)':<20} {'Size (in bytes)':<15}")
    for result in results:
        print(f"{result[0]:<25} {result[1]:<15} {result[2]:<15} {result[3]:<20} {result[4]:<15}")

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
