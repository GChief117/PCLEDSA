import os
import sys
import time

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

# Binary Search Tree Node class
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BSTNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self._insert_recursive(node.right, data)

    # In-order traversal (left, root, right)
    def in_order_traversal(self):
        def traverse(node):
            if node:
                traverse(node.left)
                print(f"In-order: {node.data} bytes")
                traverse(node.right)
        print("\nIn-order Traversal:")
        start_time = time.time()
        traverse(self.root)
        end_time = time.time()
        print(f"Time taken for in-order traversal: {end_time - start_time:.6f} seconds")

    # Pre-order traversal (root, left, right)
    def pre_order_traversal(self):
        def traverse(node):
            if node:
                print(f"Pre-order: {node.data} bytes")
                traverse(node.left)
                traverse(node.right)
        print("\nPre-order Traversal:")
        start_time = time.time()
        traverse(self.root)
        end_time = time.time()
        print(f"Time taken for pre-order traversal: {end_time - start_time:.6f} seconds")

    # Post-order traversal (left, right, root)
    def post_order_traversal(self):
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                print(f"Post-order: {node.data} bytes")
        print("\nPost-order Traversal:")
        start_time = time.time()
        traverse(self.root)
        end_time = time.time()
        print(f"Time taken for post-order traversal: {end_time - start_time:.6f} seconds")

# Function to traverse the directory and insert file sizes into a BST
def traverse_directory_for_bst(root_directory):
    bst = BinarySearchTree()

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                bst.insert(file_size)
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for the BST
    space_used_bst = sys.getsizeof(bst)
    print(f"Space complexity for BST: {space_used_bst} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return bst

# Main function to run Karatsuba algorithm with BST
def run_karatsuba_with_bst(root_directory):
    # Traverse the directory and insert file sizes into a BST
    bst = traverse_directory_for_bst(root_directory)

    # Perform in-order, pre-order, and post-order traversals
    bst.in_order_traversal()
    bst.pre_order_traversal()
    bst.post_order_traversal()

    # Collect all file sizes for Karatsuba multiplication
    def collect_file_sizes(node, file_sizes):
        if node:
            collect_file_sizes(node.left, file_sizes)
            file_sizes.append(node.data)
            collect_file_sizes(node.right, file_sizes)

    file_sizes = []
    collect_file_sizes(bst.root, file_sizes)

    # Select two largest file sizes for Karatsuba multiplication
    if len(file_sizes) >= 2:
        x, y = sorted(file_sizes)[-2:]
        print(f"\nMultiplying {x} and {y} using Karatsuba Algorithm")
        result = karatsuba(x, y)
        print(f"Result of Karatsuba multiplication: {result}")
    else:
        print("Not enough files to perform Karatsuba multiplication")

# Example usage for Karatsuba algorithm with BST
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_karatsuba_with_bst(root_directory)
