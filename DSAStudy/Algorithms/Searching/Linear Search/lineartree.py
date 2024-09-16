import os
import sys
import time

# Linear Search function
def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index
    return -1

# Regular Tree Node class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Regular Tree class
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

    # Collect all paths from the tree by visiting each node and its children
    def collect_paths(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.data)
            for child in node.children:
                self.collect_paths(child, result)
        return result

# Apply linear search on the tree and measure space and time complexity
def apply_linear_search_regular_tree(root_directory, target):
    tree = Tree()

    # Step 1: Build the tree from the directory structure
    parent_map = {}
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if tree.root is None:
            parent_map[dirpath] = tree.insert(dirpath)  # Set root node
        else:
            parent = parent_map[dirpath]
        for dirname in dirnames:
            child = tree.insert(os.path.join(dirpath, dirname), parent)
            parent_map[os.path.join(dirpath, dirname)] = child
        for filename in filenames:
            tree.insert(os.path.join(dirpath, filename), parent)

    # Step 2: Collect all paths from the tree
    print("\nCollecting paths from the regular tree:")
    paths = tree.collect_paths(tree.root)
    
    # Measure space complexity
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes")

    # Measure time taken to perform linear search
    start_time = time.time()
    index = linear_search(paths, target)
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to perform linear search: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n)")

    if index != -1:
        print(f"Target found at index {index}: {paths[index]}")
    else:
        print("Target not found")

# Example usage for a regular tree
root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory path
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_linear_search_regular_tree(root_directory, target)
