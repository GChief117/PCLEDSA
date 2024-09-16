import os
import sys
import time

# Tree node class
class TreeNode:
    def __init__(self, data):
        self.data = data
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

    def collect_file_sizes(self):
        file_sizes = []

        # Traverse the tree recursively
        def traverse(node):
            if node:
                file_sizes.append(node.data)
                for child in node.children:
                    traverse(child)

        traverse(self.root)
        return file_sizes

# Karatsuba multiplication function
def karatsuba(x, y):
    # Start timing the Karatsuba multiplication
    start_time = time.time()

    if x < 10 or y < 10:
        result = x * y
    else:
        m = min(len(str(x)), len(str(y)))
        m2 = m // 2

        high1, low1 = divmod(x, 10**m2)
        high2, low2 = divmod(y, 10**m2)

        z0 = karatsuba(low1, low2)
        z1 = karatsuba((low1 + high1), (low2 + high2))
        z2 = karatsuba(high1, high2)

        result = (z2 * 10**(2 * m2)) + ((z1 - z2 - z0) * 10**m2) + z0

    end_time = time.time()
    print(f"Time taken for Karatsuba multiplication: {end_time - start_time:.6f} seconds")
    print(f"Time complexity: O(n^1.585)")
    return result

# Function to traverse the directory and collect file sizes using a tree
def traverse_directory_for_tree(root_directory):
    tree = Tree()

    # Start timing the traversal
    start_time = time.time()

    parent_map = {}
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if tree.root is None:
            parent_map[dirpath] = tree.insert(len(dirpath))

        # Add subdirectories and files as tree nodes
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            subdir_node = tree.insert(len(subdir_path), parent_map[dirpath])
            parent_map[subdir_path] = subdir_node

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                tree.insert(file_size, parent_map[dirpath])
            except OSError:
                continue

    end_time = time.time()
    print(f"Time taken for directory traversal: {end_time - start_time:.6f} seconds")

    # Measure space complexity for the tree
    space_used = sys.getsizeof(tree)
    print(f"Space complexity for tree: {space_used} bytes")

    return tree

# Main function to run Karatsuba algorithm with tree
def run_karatsuba_with_tree(root_directory):
    # Traverse the directory and collect file sizes
    tree = traverse_directory_for_tree(root_directory)
    file_sizes = tree.collect_file_sizes()

    # Select two largest file sizes for Karatsuba multiplication
    if len(file_sizes) >= 2:
        x, y = sorted(file_sizes)[-2:]
        print(f"Multiplying {x} and {y} using Karatsuba Algorithm")
        result = karatsuba(x, y)
        print(f"Result of Karatsuba multiplication: {result}")
    else:
        print("Not enough files to perform Karatsuba multiplication")

# Example usage for Karatsuba algorithm with tree
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_karatsuba_with_tree(root_directory)
