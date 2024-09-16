import os
import sys
import time

# Graph node class
class GraphNode:
    def __init__(self, data):
        self.data = data  # File size
        self.adjacent = []  # Edges to other nodes (directories/files)

    def add_neighbor(self, neighbor):
        self.adjacent.append(neighbor)

# Graph class
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, data):
        if data not in self.nodes:
            new_node = GraphNode(data)
            self.nodes[data] = new_node
        return self.nodes[data]

    def add_edge(self, from_node, to_node):
        from_node.add_neighbor(to_node)

    def collect_weights(self):
        weights = []
        for node in self.nodes.values():
            weights.append(node.data)
        return weights

# Binary search function for graph (converted to sorted list)
def binary_search(sorted_weights):
    low, high = 0, len(sorted_weights) - 1

    # Start timing the binary search
    start_time = time.time()

    while low <= high:
        mid = (low + high) // 2
        print(f"Processing file size at index {mid}: {sorted_weights[mid]} bytes")
        low = mid + 1

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to perform binary search: {time_taken:.6f} seconds")
    print(f"Time complexity: O(log n), where n = {len(sorted_weights)}")

# Function to traverse the directory and insert file sizes into a graph
def traverse_directory_for_graph(root_directory):
    graph = Graph()

    # Start timing the traversal
    start_time = time.time()

    parent_map = {}  # To track parent-child relationships in the graph
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if dirpath not in graph.nodes:
            parent_map[dirpath] = graph.add_node(len(dirpath))  # Add the parent directory as a node

        # Add subdirectories and files as edges
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            subdir_node = graph.add_node(len(subdir_path))
            graph.add_edge(parent_map[dirpath], subdir_node)
            parent_map[subdir_path] = subdir_node

        # Add files as nodes
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                file_node = graph.add_node(file_size)
                graph.add_edge(parent_map[dirpath], file_node)
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for the graph
    space_used_graph = sys.getsizeof(graph)
    print(f"Space complexity for graph: {space_used_graph} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return graph

# Main function for binary search with graph
def run_binary_search_with_graph(root_directory):
    # Traverse the directory and collect file sizes
    graph = traverse_directory_for_graph(root_directory)

    # Collect weights (file sizes) from the graph and sort them
    weights = graph.collect_weights()
    sorted_weights = sorted(weights)

    # Perform binary search on sorted weights
    binary_search(sorted_weights)

# Example usage for binary search with graph
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_binary_search_with_graph(root_directory)
