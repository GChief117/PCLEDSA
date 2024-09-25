import os
import time
import sys
from collections import deque

# General Tree implementation for storing paths
class Tree:
    class Node:
        def __init__(self, data):
            self.data = data  # Store the path in the node
            self.children = []  # List to store children of the node

    def __init__(self):
        self.root = None  # Initialize the root of the tree

    # Insert a new path into the tree
    def insert(self, data, parent=None):
        new_node = self.Node(data)
        if parent is None:
            if self.root is None:
                self.root = new_node  # Create the root node
            else:
                self.root.children.append(new_node)  # Add to root's children if no parent is provided
        else:
            parent.children.append(new_node)  # Add to the parent's children
        return new_node

    # Pre-order traversal of the tree (root -> children)
    def pre_order_traversal(self, node):
        if node is not None:
            for child in node.children:
                self.pre_order_traversal(child)

    # Post-order traversal of the tree (children -> root)
    def post_order_traversal(self, node):
        if node is not None:
            for child in node.children:
                self.post_order_traversal(child)

    # In-order traversal for a general tree
    def in_order_traversal(self, node):
        if node is not None:
            half = len(node.children) // 2
            for child in node.children[:half]:
                self.in_order_traversal(child)
            for child in node.children[half:]:
                self.in_order_traversal(child)

    # Breadth-First Search (BFS)
    def breadth_first_search(self):
        if self.root is None:
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            for child in node.children:
                queue.append(child)

    # Depth-First Search (DFS)
    def depth_first_search(self):
        if self.root is None:
            return

        stack = [self.root]
        while stack:
            node = stack.pop()
            for child in reversed(node.children):
                stack.append(child)

# Collect all paths in the directory into the general tree
def collect_paths_into_tree(root_directory):
    tree = Tree()
    
    root_node = tree.insert(root_directory)  # Insert the root directory as the root of the tree
    
    for dirpath, dirnames, filenames in os.walk(root_directory):
        parent_node = tree.insert(dirpath, root_node)  # Insert directory path into the tree
        
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            tree.insert(file_path, parent_node)
    
    return tree

# Function to perform operations and measure time and space complexity
def perform_operations_on_tree(tree):
    # Measure space complexity
    space_used = sys.getsizeof(tree)
    
    # Store operation results for output
    results = []

    # Pre-order traversal
    start_time = time.time()
    tree.pre_order_traversal(tree.root)
    end_time = time.time()
    time_taken = end_time - start_time
    results.append(["Pre-order Traversal", "O(n)", "O(n)", f"{time_taken:.6f} seconds", f"{space_used} bytes"])

    # Post-order traversal
    start_time = time.time()
    tree.post_order_traversal(tree.root)
    end_time = time.time()
    time_taken = end_time - start_time
    results.append(["Post-order Traversal", "O(n)", "O(n)", f"{time_taken:.6f} seconds", f"{space_used} bytes"])

    # In-order traversal
    start_time = time.time()
    tree.in_order_traversal(tree.root)
    end_time = time.time()
    time_taken = end_time - start_time
    results.append(["In-order Traversal", "O(n)", "O(n)", f"{time_taken:.6f} seconds", f"{space_used} bytes"])

    # Breadth-First Search (BFS)
    start_time = time.time()
    tree.breadth_first_search()
    end_time = time.time()
    time_taken = end_time - start_time
    results.append(["BFS Traversal", "O(n)", "O(n)", f"{time_taken:.6f} seconds", f"{space_used} bytes"])

    # Depth-First Search (DFS)
    start_time = time.time()
    tree.depth_first_search()
    end_time = time.time()
    time_taken = end_time - start_time
    results.append(["DFS Traversal", "O(n)", "O(n)", f"{time_taken:.6f} seconds", f"{space_used} bytes"])

    # Print the formatted results for Excel
    print(f"{'Operation':<25} {'Time Complexity':<15} {'Space Complexity':<15} {'Time (in seconds)':<20} {'Size (in bytes)':<15}")
    for result in results:
        print(f"{result[0]:<25} {result[1]:<15} {result[2]:<15} {result[3]:<20} {result[4]:<15}")

# Main function
def main():
    # Define the root directory (adjust this to your actual directory path)
    root_directory = "/Volumes/CD/pCLE"
    
    # Step 1: Collect all paths into the tree
    tree = collect_paths_into_tree(root_directory)
    
    # Step 2: Perform operations on the tree and measure complexities
    perform_operations_on_tree(tree)

# Run the main function
if __name__ == "__main__":
    main()
