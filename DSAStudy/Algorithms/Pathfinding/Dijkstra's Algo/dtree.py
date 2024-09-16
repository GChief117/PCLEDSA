import os
import sys
import heapq
import time

# Tree Node class with weights (for Dijkstra-like application)
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child, weight):
        self.children.append((child, weight))

# Tree class
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data, parent=None, weight=0):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
        elif parent:
            parent.add_child(new_node, weight)
        return new_node

    # Dijkstra-like algorithm for trees
    def dijkstra_tree(self, start_node):
        distances = {self.root: float('inf')}
        distances[start_node] = 0
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            for child, weight in current_node.children:
                distance = current_distance + weight
                if distance < distances.get(child, float('inf')):
                    distances[child] = distance
                    heapq.heappush(priority_queue, (distance, child))

        return distances

# Apply Dijkstra-like algorithm on the tree and measure space and time complexity
def apply_dijkstra_tree(root_directory, target):
    tree = Tree()

    # Step 1: Build the tree from the directory structure
    parent_map = {}
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if tree.root is None:
            parent_map[dirpath] = tree.insert(dirpath)  # Set root node
        else:
            parent = parent_map[dirpath]
        for dirname in dirnames:
            child = tree.insert(os.path.join(dirpath, dirname), parent, 1)
            parent_map[os.path.join(dirpath, dirname)] = child
        for filename in filenames:
            tree.insert(os.path.join(dirpath, filename), parent, 1)

    # Step 2: Perform Dijkstra-like algorithm from the root
    print("\nRunning Dijkstra-like Algorithm on the Tree:")
    start_node = tree.root
    perform_dijkstra_tree_with_metrics(tree, start_node, target)

# Perform Dijkstra-like algorithm and measure space and time complexity for the tree
def perform_dijkstra_tree_with_metrics(tree, start_node, target):
    # Measure space complexity
    space_used = sys.getsizeof(tree)
    print(f"Space complexity: {space_used} bytes (for the tree)")

    # Measure time taken to run the Dijkstra-like algorithm
    start_time = time.time()
    distances = tree.dijkstra_tree(start_node)
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to run Dijkstra-like algorithm: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n log n)")

    # Output the distances between the start node and target (if found)
    for node, distance in distances.items():
        if node.data == target:
            print(f"Shortest distance from {start_node.data} to {target}: {distance}")
            return

    print(f"Target {target} not found in the tree.")

# Example usage for the tree
root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory path
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_dijkstra_tree(root_directory, target)
