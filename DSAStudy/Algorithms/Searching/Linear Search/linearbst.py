import os
import sys
import time

# Linear Search function
def linear_search(arr, target):
    for index, item in enumerate(arr):
        if item == target:
            return index
    return -1

# Binary Search Tree (BST) class
class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            self._insert_recursive(self.root, data)

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

    # In-order traversal to collect paths
    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.data)
            self.in_order_traversal(node.right, result)
        return result

    # Pre-order traversal to collect paths
    def pre_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.data)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    # Post-order traversal to collect paths
    def post_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.data)
        return result

# Apply linear search on the sorted paths from different traversals
def apply_linear_search_bst_traversals(root_directory, target):
    bst = BST()

    # Step 1: Collect paths and insert into BST
    for dirpath, dirnames, filenames in os.walk(root_directory):
        bst.insert(dirpath)
        for filename in filenames:
            bst.insert(os.path.join(dirpath, filename))

    # Step 2: Perform In-order traversal
    print("\nIn-order Traversal:")
    in_order_paths = bst.in_order_traversal(bst.root)
    perform_linear_search_with_metrics(in_order_paths, target)

    # Step 3: Perform Pre-order traversal
    print("\nPre-order Traversal:")
    pre_order_paths = bst.pre_order_traversal(bst.root)
    perform_linear_search_with_metrics(pre_order_paths, target)

    # Step 4: Perform Post-order traversal
    print("\nPost-order Traversal:")
    post_order_paths = bst.post_order_traversal(bst.root)
    perform_linear_search_with_metrics(post_order_paths, target)

# Perform linear search with space and time complexity measurements
def perform_linear_search_with_metrics(paths, target):
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

# Example usage for BST with all traversals
root_directory = "/Volumes/CD/pCLE"
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_linear_search_bst_traversals(root_directory, target)
