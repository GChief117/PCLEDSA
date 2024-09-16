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

    # QuickSort function for paths from any traversal
    def quicksort_paths(self, paths):
        # Measure space complexity
        space_used = sys.getsizeof(paths)
        print(f"Space complexity: {space_used} bytes")

        # Measure time taken to apply QuickSort
        start_time = time.time()
        sorted_paths = quicksort(paths)  # Use QuickSort function
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply QuickSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Output sorted paths
        for path in sorted_paths:
            print(f"Processing path: {path}")

# QuickSort function
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Collect all paths in the directory and insert into the BST
def collect_paths_bst(root_directory):
    bst = BST()
    for dirpath, dirnames, filenames in os.walk(root_directory):
        bst.insert(dirpath)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            bst.insert(file_path)
    return bst

# Apply all three traversals (in-order, pre-order, and post-order) and QuickSort
def process_bst_with_quicksort(root_directory):
    bst = collect_paths_bst(root_directory)

    # In-order Traversal and QuickSort
    print("\nIn-order Traversal and QuickSort:")
    in_order_paths = bst.in_order_traversal(bst.root)
    bst.quicksort_paths(in_order_paths)

    # Pre-order Traversal and QuickSort
    print("\nPre-order Traversal and QuickSort:")
    pre_order_paths = bst.pre_order_traversal(bst.root)
    bst.quicksort_paths(pre_order_paths)

    # Post-order Traversal and QuickSort
    print("\nPost-order Traversal and QuickSort:")
    post_order_paths = bst.post_order_traversal(bst.root)
    bst.quicksort_paths(post_order_paths)

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory path
process_bst_with_quicksort(root_directory)
