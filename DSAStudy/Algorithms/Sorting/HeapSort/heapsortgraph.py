import os
import time
import sys
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Add edges between directories and files
    def add_edge(self, node, neighbor):
        self.graph[node].append(neighbor)

    # Collect all paths from the graph into a list for sorting
    def collect_paths(self):
        paths = list(self.graph.keys())
        for node, neighbors in self.graph.items():
            paths.extend(neighbors)
        return paths

    # HeapSort function for the graph
    def heap_sort_graph(self):
        # Collect all paths from the graph
        paths = self.collect_paths()

        # Measure space complexity
        space_used = sys.getsizeof(paths)
        print(f"Space complexity: {space_used} bytes (for the graph)")

        # Measure time taken to apply HeapSort
        start_time = time.time()
        sorted_paths = heap_sort(paths)
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply HeapSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Output sorted paths
        for path in sorted_paths:
            print(f"Processing path: {path}")

# Collect all paths in the directory into a graph
def collect_paths_graph(root_directory):
    graph = Graph()
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for dirname in dirnames:
            graph.add_edge(dirpath, os.path.join(dirpath, dirname))
        for filename in filenames:
            graph.add_edge(dirpath, os.path.join(dirpath, filename))
    return graph

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory path
graph = collect_paths_graph(root_directory)
graph.heap_sort_graph()
