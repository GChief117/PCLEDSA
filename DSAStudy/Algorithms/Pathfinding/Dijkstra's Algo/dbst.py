import os
import sys
import heapq
import time

# Binary Search Tree (BST) Node class
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

    # In-order traversal for collecting paths
    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.data)
            self.in_order_traversal(node.right, result)
        return result

    # Pre-order traversal for collecting paths
    def pre_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            result.append(node.data)
            self.pre_order_traversal(node.left, result)
            self.pre_order_traversal(node.right, result)
        return result

    # Post-order traversal for collecting paths
    def post_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.post_order_traversal(node.left, result)
            self.post_order_traversal(node.right, result)
            result.append(node.data)
        return result

# Adapt Dijkstra-like algorithm for paths collected via traversals in BST
def dijkstra_bst(paths, start):
    distances = {path: float('inf') for path in paths}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_path = heapq.heappop(priority_queue)

        # Assuming neighboring paths are sequential in this case
        current_index = paths.index(current_path)
        if current_index + 1 < len(paths):
            neighbor = paths[current_index + 1]
            distance = current_distance + 1  # Weight of 1 for simplicity
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Apply Dijkstra's Algorithm on the collected BST paths
def apply_dijkstra_bst_traversals(root_directory, target):
    bst = BST()

    # Build the BST from the root directory structure
    for dirpath, dirnames, filenames in os.walk(root_directory):
        bst.insert(dirpath)
        for filename in filenames:
            bst.insert(os.path.join(dirpath, filename))

    # In-order Traversal
    print("\nIn-order Traversal:")
    in_order_paths = bst.in_order_traversal(bst.root)
    perform_dijkstra_with_metrics(in_order_paths, target)

    # Pre-order Traversal
    print("\nPre-order Traversal:")
    pre_order_paths = bst.pre_order_traversal(bst.root)
    perform_dijkstra_with_metrics(pre_order_paths, target)

    # Post-order Traversal
    print("\nPost-order Traversal:")
    post_order_paths = bst.post_order_traversal(bst.root)
    perform_dijkstra_with_metrics(post_order_paths, target)

# Perform Dijkstra-like algorithm and measure space and time complexity
def perform_dijkstra_with_metrics(paths, start_node):
    # Measure space complexity
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes")

    # Measure time taken to run the Dijkstra-like algorithm
    start_time = time.time()
    distances = dijkstra_bst(paths, start_node)
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to run Dijkstra-like algorithm: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n log n)")

    # Output the distances between the paths
    for node, distance in distances.items():
        print(f"Distance from {start_node} to {node}: {distance}")

# Example usage for BST with all traversals
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_dijkstra_bst_traversals(root_directory, target)
