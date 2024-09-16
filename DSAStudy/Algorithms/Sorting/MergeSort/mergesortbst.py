import os
import time
import sys

class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    # Insert a new node into the BST
    def insert(self, data):
        if not self.root:
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

    # MergeSort for paths from any traversal
    def merge_sort_paths(self, paths):
        # Measure space complexity
        space_used = sys.getsizeof(paths)
        print(f"Space complexity: {space_used} bytes")

        # Measure time taken to apply MergeSort
        start_time = time.time()
        sorted_paths = merge_sort(paths)  # Use MergeSort function
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply MergeSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Output sorted paths
        for path in sorted_paths:
            print(f"Processing path: {path}")

# MergeSort function
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Merge function to merge two sorted subarrays
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Collect all paths in the directory and insert into the BST
def collect_paths_bst(root_directory):
    bst = BST()
    for dirpath, dirnames, filenames in os.walk(root_directory):
        bst.insert(dirpath)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            bst.insert(file_path)
    return bst

# Apply all three traversals (in-order, pre-order, and post-order) and MergeSort
def process_bst_with_mergesort(root_directory):
    bst = collect_paths_bst(root_directory)

    # In-order Traversal and MergeSort
    print("\nIn-order Traversal and MergeSort:")
    in_order_paths = bst.in_order_traversal(bst.root)
    bst.merge_sort_paths(in_order_paths)

    # Pre-order Traversal and MergeSort
    print("\nPre-order Traversal and MergeSort:")
    pre_order_paths = bst.pre_order_traversal(bst.root)
    bst.merge_sort_paths(pre_order_paths)

    # Post-order Traversal and MergeSort
    print("\nPost-order Traversal and MergeSort:")
    post_order_paths = bst.post_order_traversal(bst.root)
    bst.merge_sort_paths(post_order_paths)

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory path
process_bst_with_mergesort(root_directory)
