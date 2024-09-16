import os
import sys
import time
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Add edges between directories and files
    def add_edge(self, node, neighbor):
        self.graph[node].append(neighbor)

    # Collect all paths from the graph into a list for sorting and binary search
    def collect_paths(self):
        paths = list(self.graph.keys())
        for node in self.graph:
            paths.extend(self.graph[node])
        return paths

    # Apply binary search on the graph paths
    def binary_search_graph(self, paths, target):
        paths.sort()  # Sort the paths for binary search
        low, high = 0, len(paths) - 1

        while low <= high:
            mid = (low + high) // 2
            if paths[mid] == target:
                return mid
            elif paths[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# Apply binary search on the graph and measure space and time complexity
def apply_binary_search_graph(root_directory, target):
    graph = Graph()

    # Step 1: Build graph from the directory structure
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for dirname in dirnames:
            graph.add_edge(dirpath, os.path.join(dirpath, dirname))
        for filename in filenames:
            graph.add_edge(dirpath, os.path.join(dirpath, filename))

    # Step 2: Collect paths from graph
    paths = graph.collect_paths()

    # Step 3: Apply binary search
    index = graph.binary_search_graph(paths, target)

    # Measure space complexity
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes (for the graph)")

    # Measure time complexity
    start_time = time.time()
    index = graph.binary_search_graph(paths, target)
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to perform binary search: {time_taken:.6f} seconds")
    print(f"Time complexity: O(log n)")

    if index != -1:
        print(f"Target found at index {index}")
    else:
        print("Target not found")

# Example usage for graphs
root_directory = "/Volumes/CD/pCLE"
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_binary_search_graph(root_directory, target)
