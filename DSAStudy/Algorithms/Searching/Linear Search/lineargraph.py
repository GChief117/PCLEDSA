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

    # Collect all paths from the graph into a list for searching
    def collect_paths(self):
        paths = list(self.graph.keys())
        for node in self.graph:
            paths.extend(self.graph[node])
        return paths

# Apply linear search on the graph and measure space and time complexity
def apply_linear_search_graph(root_directory, target):
    graph = Graph()

    # Step 1: Build graph from the directory structure
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for dirname in dirnames:
            graph.add_edge(dirpath, os.path.join(dirpath, dirname))
        for filename in filenames:
            graph.add_edge(dirpath, os.path.join(dirpath, filename))

    # Step 2: Collect paths from the graph
    paths = graph.collect_paths()

    # Measure space complexity
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes (for the graph)")

    # Measure time complexity
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

# Example usage for graphs
root_directory = "/Volumes/CD/pCLE"
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_linear_search_graph(root_directory, target)
