import os
import sys
import time

# Balanced Binary Search Tree Node class
class BSTNode:
    def __init__(self, file_path, file_size):
        self.file_path = file_path
        self.file_size = file_size
        self.left = None
        self.right = None

# Balanced Binary Search Tree class
class BalancedBST:
    def __init__(self):
        self.root = None

    def insert_balanced(self, file_paths_sizes):
        self.root = self._build_balanced_tree(sorted(file_paths_sizes), 0, len(file_paths_sizes) - 1)

    def _build_balanced_tree(self, file_paths_sizes, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        file_path, file_size = file_paths_sizes[mid]
        node = BSTNode(file_path, file_size)
        node.left = self._build_balanced_tree(file_paths_sizes, start, mid - 1)
        node.right = self._build_balanced_tree(file_paths_sizes, mid + 1, end)
        return node

    # In-order traversal (Left, Root, Right)
    def in_order_traversal(self):
        print("\nIn-order Traversal (Balanced):")
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
        print("\nPre-order Traversal (Balanced):")
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
        print("\nPost-order Traversal (Balanced):")
        start_time = time.time()

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                print(f"Post-order: {node.file_path} ({node.file_size} bytes)")

        traverse(self.root)

        end_time = time.time()
        print(f"Time taken for post-order traversal: {end_time - start_time:.6f} seconds")


# Function to traverse the directory and insert files into a balanced BST
def traverse_directory_for_balanced_bst(root_directory):
    file_paths_sizes = []

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                file_paths_sizes.append((file_path, file_size))
            except OSError:
                continue

    end_time = time.time()
    print(f"Time taken for directory traversal: {end_time - start_time:.6f} seconds")

    # Measure space complexity for file size collection
    space_used_list = sys.getsizeof(file_paths_sizes)
    print(f"Space complexity for file collection: {space_used_list} bytes")

    bst = BalancedBST()
    bst.insert_balanced(file_paths_sizes)
    return bst

# Main function to perform file insertion and all traversals for a balanced BST
def run_file_insertion_with_balanced_bst(root_directory):
    # Traverse the directory and insert files into a balanced BST
    bst = traverse_directory_for_balanced_bst(root_directory)

    # Perform in-order, pre-order, and post-order traversals
    bst.in_order_traversal()
    bst.pre_order_traversal()
    bst.post_order_traversal()

# Example usage for balanced BST
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_file_insertion_with_balanced_bst(root_directory)
