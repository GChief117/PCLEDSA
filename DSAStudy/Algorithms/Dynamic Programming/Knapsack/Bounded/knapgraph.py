import os
import sys
import time

# Bounded Knapsack dynamic programming function
def bounded_knapsack(values, weights, counts, capacity):
    n = len(values)
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Start timing the knapsack computation
    start_time = time.time()

    # Build the table considering bounded counts for each item
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            for k in range(counts[i - 1] + 1):  # Check k copies of the item
                if k * weights[i - 1] <= w:
                    dp_table[i][w] = max(dp_table[i][w], dp_table[i - 1][w - k * weights[i - 1]] + k * values[i - 1])

    end_time = time.time()
    time_taken = end_time - start_time

    # Output time complexity
    print(f"Time taken to compute bounded knapsack: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n * W * c), where n = {n}, W = {capacity}, c = counts")

    # Measure space complexity
    space_used = sys.getsizeof(dp_table)
    print(f"Space complexity: {space_used} bytes for the dp table")

    # The last entry contains the maximum value we can achieve
    return dp_table[n][capacity]

# Graph node class
class GraphNode:
    def __init__(self, data, weight, value, count):
        self.data = data
        self.weight = weight
        self.value = value
        self.count = count  # Bounded constraint (number of copies)
        self.adjacent = []  # Stores edges to other nodes

    def add_neighbor(self, neighbor):
        self.adjacent.append(neighbor)

# Graph class
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, data, weight, value, count):
        if data not in self.nodes:
            new_node = GraphNode(data, weight, value, count)
            self.nodes[data] = new_node
        return self.nodes[data]

    def add_edge(self, from_node, to_node):
        from_node.add_neighbor(to_node)

    def traverse_graph(self):
        weights = []
        values = []
        counts = []
        total_capacity = 0

        # Traverse all nodes in the graph
        for node in self.nodes.values():
            weights.append(node.weight)
            values.append(node.value)
            counts.append(node.count)
            total_capacity += node.weight

        return weights, values, counts, total_capacity

# Function to traverse the directory and insert into a graph
def insert_in_graph_bounded(root_directory):
    graph = Graph()
    total_capacity = 0

    # Start timing the traversal
    start_time = time.time()

    # Traverse the directory structure and collect file paths and sizes
    parent_map = {}  # To keep track of parent-child relationships in the graph
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if dirpath not in graph.nodes:
            parent_map[dirpath] = graph.add_node(dirpath, len(dirpath), len(dirpath), 1)  # Create parent node

        # Add subdirectories as edges
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            subdir_node = graph.add_node(subdir_path, len(subdir_path), len(subdir_path), 1)
            graph.add_edge(parent_map[dirpath], subdir_node)
            parent_map[subdir_path] = subdir_node

        # Add files as edges
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                file_node = graph.add_node(file_path, file_size, file_size, 3)  # Example: 3 copies of each file
                graph.add_edge(parent_map[dirpath], file_node)
                total_capacity += file_size
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for the graph
    space_used_graph = sys.getsizeof(graph)
    print(f"Space complexity for graph: {space_used_graph} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return graph

# Main function to run bounded knapsack with graph and dynamic capacity
def run_bounded_knapsack_with_graph(root_directory):
    # Traverse the directory and insert data into the graph
    graph = insert_in_graph_bounded(root_directory)

    # Retrieve weights, values, and counts from the graph
    weights, values, counts, total_capacity = graph.traverse_graph()

    # Apply the bounded knapsack algorithm with the dynamically calculated total capacity
    max_value = bounded_knapsack(values, weights, counts, total_capacity)
    print(f"Maximum value achievable with bounded knapsack: {max_value}")

# Example usage for bounded knapsack with graph
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_bounded_knapsack_with_graph(root_directory)
