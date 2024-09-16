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

    # HeapSort for paths from any traversal
    def heap_sort_paths(self, paths):
        # Measure space complexity
        space_used = sys.getsizeof(paths)
        print(f"Space complexity: {space_used} bytes")

        # Measure time taken to apply HeapSort
        start_time = time.time()
        sorted_paths = heap_sort(paths)  # Use HeapSort function
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply HeapSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Output sorted paths
        for path in sorted_paths:
            print(f"Processing path: {path}")

# HeapSort function for an array
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Collect all paths in the directory and insert them into the BST
def collect_paths_bst(root_directory):
    bst = BST()
    for dirpath, dirnames, filenames in os.walk(root_directory):
        bst.insert(dirpath)
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            bst.insert(file_path)
    return bst

# Apply all three traversals (in-order, pre-order, and post-order) and HeapSort
def process_bst_with_heapsort(root_directory):
    bst = collect_paths_bst(root_directory)

    # In-order Traversal and HeapSort
    print("\nIn-order Traversal and HeapSort:")
    in_order_paths = bst.in_order_traversal(bst.root)
    bst.heap_sort_paths(in_order_paths)

    # Pre-order Traversal and HeapSort
    print("\nPre-order Traversal and HeapSort:")
    pre_order_paths = bst.pre_order_traversal(bst.root)
    bst.heap_sort_paths(pre_order_paths)

    # Post-order Traversal and HeapSort
    print("\nPost-order Traversal and HeapSort:")
    post_order_paths = bst.post_order_traversal(bst.root)
    bst.heap_sort_paths(post_order_paths)

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory path
process_bst_with_heapsort(root_directory)
