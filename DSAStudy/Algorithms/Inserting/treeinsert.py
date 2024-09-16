import os
import sys
import time

class TreeNode:
    def __init__(self, file_path, file_size):
        self.file_path = file_path
        self.file_size = file_size
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, file_path, file_size, parent=None):
        new_node = TreeNode(file_path, file_size)
        if self.root is None:
            self.root = new_node
        elif parent:
            parent.add_child(new_node)
        return new_node

# Function to insert a file into a tree (simulating file insertion)
def insert_file_into_tree(tree, file_path):
    try:
        file_size = os.path.getsize(file_path)
    except OSError:
        print(f"Error retrieving file size for {file_path}")
        return

    # Start timing the insertion
    start_time = time.time()

    # Add the new file as a node in the tree
    tree.insert(file_path, file_size, parent=tree.root)

    end_time = time.time()
    print(f"Time taken for tree file insertion: {end_time - start_time:.6f} seconds")
    print(f"Time complexity: O(1)")

# Function to traverse the directory and collect files using tree
def traverse_directory_for_tree(root_directory):
    tree = Tree()
    parent_map = {}

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        if tree.root is None:
            parent_map[dirpath] = tree.insert(dirpath, len(dirpath))  # Add directory as the root

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                tree.insert(file_path, file_size, parent=parent_map[dirpath])
            except OSError:
                continue

    end_time = time.time()
    print(f"Time taken for directory traversal: {end_time - start_time:.6f} seconds")

    # Measure space complexity for tree
    space_used_tree = sys.getsizeof(tree)
    print(f"Space complexity for tree: {space_used_tree} bytes")

    return tree

# Main function to perform file insertion into tree
def run_file_insertion_with_tree(root_directory, file_to_insert):
    # Traverse the directory and collect files
    tree = traverse_directory_for_tree(root_directory)

    # Insert the new file into the tree
    print(f"\nInserting {file_to_insert} into the tree:")
    insert_file_into_tree(tree, file_to_insert)

# Example usage for tree file insertion
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    file_to_insert = "/path/to/new/file.txt"  # Replace with the path of the new file
    run_file_insertion_with_tree(root_directory, file_to_insert)
