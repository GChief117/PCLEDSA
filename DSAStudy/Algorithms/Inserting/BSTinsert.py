import sys
import os
import time

class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        start_time = time.time()  # Start the timer
        if self.root is None:
            self.root = self.Node(data)
        else:
            self._insert_recursive(self.root, data)
        end_time = time.time()  # End the timer

        # Measure space complexity
        space_used = sys.getsizeof(self.root)
        print(f"Space complexity: {space_used} bytes (for the BST)")

        # Measure time complexity
        time_taken = end_time - start_time
        print(f"Time taken to insert into BST: {time_taken:.6f} seconds")
        print(f"Time complexity: O(log n)")

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = self.Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = self.Node(data)
            else:
                self._insert_recursive(node.right, data)

    # In-order Traversal (Left, Root, Right)
    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.data)
            self.in_order_traversal(node.right, result)
        return result

    # Pre-order Traversal (Root, Left, Right)
    def pre_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.data)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    # Post-order Traversal (Left, Right, Root)
    def post_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.data)
        return result

# Apply the insertion and perform all traversals
def apply_bst_traversals(root_directory):
    bst = BST()

    # Insert all paths into BST
    print("\n--- Inserting paths into the BST ---")
    for dirpath, dirnames, filenames in os.walk(root_directory):
        bst.insert(dirpath)
        for filename in filenames:
            bst.insert(os.path.join(dirpath, filename))

    # Perform in-order traversal
    print("\n--- In-order Traversal ---")
    start_time = time.time()
    in_order_paths = bst.in_order_traversal(bst.root)
    end_time = time.time()
    print(f"Time taken for In-order Traversal: {end_time - start_time:.6f} seconds")
    for path in in_order_paths:
        print(f"Path: {path}")

    # Perform pre-order traversal
    print("\n--- Pre-order Traversal ---")
    start_time = time.time()
    pre_order_paths = bst.pre_order_traversal(bst.root)
    end_time = time.time()
    print(f"Time taken for Pre-order Traversal: {end_time - start_time:.6f} seconds")
    for path in pre_order_paths:
        print(f"Path: {path}")

    # Perform post-order traversal
    print("\n--- Post-order Traversal ---")
    start_time = time.time()
    post_order_paths = bst.post_order_traversal(bst.root)
    end_time = time.time()
    print(f"Time taken for Post-order Traversal: {end_time - start_time:.6f} seconds")
    for path in post_order_paths:
        print(f"Path: {path}")

# Example usage for the BST
root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
apply_bst_traversals(root_directory)
