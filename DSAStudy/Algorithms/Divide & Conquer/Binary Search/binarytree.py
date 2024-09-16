import os
import sys
import time

# Tree node class
class TreeNode:
    def __init__(self, data):
        self.data = data  # File size or directory length
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Tree class
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data, parent=None):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
        elif parent:
            parent.add_child(new_node)
        return new_node

    def collect_weights(self):
        weights = []

        # Traverse the tree recursively
        def traverse(node):
            if node:
                weights.append(node.data)
                for child in node.children:
                    traverse(child)

        traverse(self.root)
        return weights

# Binary search function for tree (converted to sorted list)
def binary_search(sorted_weights):
    low, high = 0, len(sorted_weights) - 1

    # Start timing the binary search
    start_time = time.time()

    while low <= high:
        mid = (low + high) // 2
        print(f"Processing file size at index {mid}: {sorted_weights[mid]} bytes")
        low = mid + 1

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to perform binary search: {time_taken:.6f} seconds")
    print(f"Time complexity: O(log n), where n = {len(sorted_weights)}")

# Function to traverse the directory and insert file sizes into a tree
def traverse_directory_for_tree(root_directory):
    tree = Tree()

    # Start timing the traversal
    start_time = time.time()

    parent_map = {}  # To track parent-child relationships in the tree
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if tree.root is None:
            parent_map[dirpath] = tree.insert(len(dirpath))  # Add the parent directory as the root

        # Add subdirectories and files as children
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            subdir_node = tree.insert(len(subdir_path), parent_map[dirpath])
            parent_map[subdir_path] = subdir_node

        # Add files as children
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                tree.insert(file_size, parent_map[dirpath])  # Insert file size as a child node
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for the tree
    space_used_tree = sys.getsizeof(tree)
    print(f"Space complexity for tree: {space_used_tree} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return tree

# Main function for binary search with tree
def run_binary_search_with_tree(root_directory):
    # Traverse the directory and collect file sizes
    tree = traverse_directory_for_tree(root_directory)

    # Collect weights (file sizes) from the tree and sort them
    weights = tree.collect_weights()
    sorted_weights = sorted(weights)

    # Perform binary search on sorted weights
    binary_search(sorted_weights)

# Example usage for binary search with tree
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_binary_search_with_tree(root_directory)
