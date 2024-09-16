import os
import time
import sys

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    # Add a child node to the tree
    def add_child(self, child_node):
        self.children.append(child_node)

class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    # Pre-order traversal to collect paths
    def flatten_tree(self, node, result=None):
        if result is None:
            result = []
        result.append(node.data)
        for child in node.children:
            self.flatten_tree(child, result)
        return result

    # HeapSort function for the tree
    def heap_sort_tree(self):
        # Flatten the tree into a list of paths
        paths = self.flatten_tree(self.root)

        # Measure space complexity
        space_used = sys.getsizeof(paths)
        print(f"Space complexity: {space_used} bytes (for the flattened tree)")

        # Measure time taken to apply HeapSort
        start_time = time.time()
        sorted_paths = heap_sort(paths)
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply HeapSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Output sorted paths
        for path in sorted_paths:
            print(f"Processing path: {path}")

# Collect all paths in the directory and insert into the tree
def collect_paths_tree(root_directory):
    tree = Tree(root_directory)
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for dirname in dirnames:
            subtree = TreeNode(os.path.join(dirpath, dirname))
            tree.root.add_child(subtree)
        for filename in filenames:
            tree.root.add_child(TreeNode(os.path.join(dirpath, filename)))
    return tree

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory path
tree = collect_paths_tree(root_directory)
tree.heap_sort_tree()
