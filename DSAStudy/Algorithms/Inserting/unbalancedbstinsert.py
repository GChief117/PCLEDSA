import os
import sys
import time

# Binary Search Tree Node class
class BSTNode:
    def __init__(self, file_path, file_size):
        self.file_path = file_path
        self.file_size = file_size
        self.left = None
        self.right = None

# Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, file_path, file_size):
        if self.root is None:
            self.root = BSTNode(file_path, file_size)
        else:
            self._insert_recursive(self.root, file_path, file_size)

    def _insert_recursive(self, node, file_path, file_size):
        if file_size < node.file_size:
            if node.left is None:
                node.left = BSTNode(file_path, file_size)
            else:
                self._insert_recursive(node.left, file_path, file_size)
        else:
            if node.right is None:
                node.right = BSTNode(file_path, file_size)
            else:
                self._insert_recursive(node.right, file_path, file_size)

    # In-order traversal (Left, Root, Right)
    def in_order_traversal(self):
        print("\nIn-order Traversal:")
        start_time = time.time()

        def traverse(node):
            if node:
                traverse(node.left)
                print(f"In-order: {node.file_path} ({node.file_size} bytes)")
                traverse(node.right)

        traverse(self.root)

        end_time = time.time()
        print(f"Time taken for in-order traversal: {end_time - start_time:.6f} seconds")

    # Pre-order traversal (Root, Left, Right)
    def pre_order_traversal(self):
        print("\nPre-order Traversal:")
        start_time = time.time()

        def traverse(node):
            if node:
                print(f"Pre-order: {node.file_path} ({node.file_size} bytes)")
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)

        end_time = time.time()
        print(f"Time taken for pre-order traversal: {end_time - start_time:.6f} seconds")

    # Post-order traversal (Left, Right, Root)
    def post_order_traversal(self):
        print("\nPost-order Traversal:")
        start_time = time.time()

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                print(f"Post-order: {node.file_path} ({node.file_size} bytes)")

        traverse(self.root)

        end_time = time.time()
        print(f"Time taken for post-order traversal: {end_time - start_time:.6f} seconds")


# Function to traverse the directory and insert files into an unbalanced BST
def traverse_directory_for_unbalanced_bst(root_directory):
    bst = BinarySearchTree()

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                bst.insert(file_path, file_size)
            except OSError:
                continue

    end_time = time.time()
    print(f"Time taken for directory traversal: {end_time - start_time:.6f} seconds")

    # Measure space complexity for BST
    space_used_bst = sys.getsizeof(bst)
    print(f"Space complexity for unbalanced BST: {space_used_bst} bytes")

    return bst

# Main function to perform file insertion and all traversals for an unbalanced BST
def run_file_insertion_with_unbalanced_bst(root_directory):
    # Traverse the directory and insert files into an unbalanced BST
    bst = traverse_directory_for_unbalanced_bst(root_directory)

    # Perform in-order, pre-order, and post-order traversals
    bst.in_order_traversal()
    bst.pre_order_traversal()
    bst.post_order_traversal()

# Example usage for unbalanced BST
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_file_insertion_with_unbalanced_bst(root_directory)
