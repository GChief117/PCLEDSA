import os
import sys
import time

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

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

# Insert directories and files into a regular tree while calculating Fibonacci
def insert_in_tree_fib(root_directory):
    tree = Tree()
    memo = {}
    parent_map = {}

    # Start processing the root directory
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if tree.root is None:
            parent_map[dirpath] = tree.insert(dirpath)  # Insert root directory
        else:
            parent = parent_map[dirpath]  # Find the parent node
            # Insert subdirectories as children
            for dirname in dirnames:
                child_node = tree.insert(os.path.join(dirpath, dirname), parent)
                parent_map[os.path.join(dirpath, dirname)] = child_node
            # Insert files as children
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                tree.insert(file_path, parent)
                
                # Calculate Fibonacci for the file path length using memoization
                fib_result = fibonacci_memo(len(file_path), memo)
                print(f"Fibonacci({len(file_path)}) result for file: {file_path} = {fib_result}")

    # Measure space complexity (space used by the tree)
    space_used = sys.getsizeof(tree)
    print(f"Space complexity: {space_used} bytes (for the regular tree)")

    # Measure time complexity for processing the tree
    start_time = time.time()
    for path, node in parent_map.items():
        fibonacci_memo(len(path), memo)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to process tree: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n)")

    # Print the tree structure
    def print_tree(node, level=0):
        print("  " * level + f"Node: {node.data}")
        for child in node.children:
            print_tree(child, level + 1)

    print("\n--- Tree Structure ---")
    print_tree(tree.root)

# Example usage for the regular tree
root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
insert_in_tree_fib(root_directory)
