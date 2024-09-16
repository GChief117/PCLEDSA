import os
import sys
import time

# Knapsack dynamic programming function
def knapsack(values, weights, capacity):
    n = len(values)
    dp_table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Start timing the knapsack computation
    start_time = time.time()

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp_table[i][w] = max(values[i - 1] + dp_table[i - 1][w - weights[i - 1]], dp_table[i - 1][w])
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    end_time = time.time()
    time_taken = end_time - start_time

    # Output time complexity
    print(f"Time taken to compute knapsack: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n * W), where n = {n}, W = {capacity}")

    # Measure space complexity
    space_used = sys.getsizeof(dp_table)
    print(f"Space complexity: {space_used} bytes for the dp table")

    # The last entry contains the maximum value we can achieve
    return dp_table[n][capacity]

# Graph node class
class GraphNode:
    def __init__(self, data, weight, value):
        self.data = data
        self.weight = weight
        self.value = value
        self.adjacent = []  # Stores edges to other nodes (neighbors)

    def add_neighbor(self, neighbor):
        self.adjacent.append(neighbor)

# Graph class
class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, data, weight, value):
        if data not in self.nodes:
            new_node = GraphNode(data, weight, value)
            self.nodes[data] = new_node
        return self.nodes[data]

    def add_edge(self, from_node, to_node):
        from_node.add_neighbor(to_node)

    def traverse_graph(self):
        total_weight = 0
        total_value = 0
        weights = []
        values = []

        # Traverse all nodes in the graph
        for node in self.nodes.values():
            weights.append(node.weight)
            values.append(node.value)
            total_weight += node.weight
            total_value += node.value

        return weights, values, total_weight

# Function to traverse the directory and insert into a graph
def insert_in_graph(root_directory):
    graph = Graph()
    total_capacity = 0

    # Start timing the traversal
    start_time = time.time()

    # Traverse the directory structure and collect file paths and sizes
    parent_map = {}  # To keep track of parent-child relationships in the graph
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if dirpath not in graph.nodes:
            parent_map[dirpath] = graph.add_node(dirpath, len(dirpath), len(dirpath))  # Create parent node

        # Add subdirectories as edges
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            subdir_node = graph.add_node(subdir_path, len(subdir_path), len(subdir_path))
            graph.add_edge(parent_map[dirpath], subdir_node)
            parent_map[subdir_path] = subdir_node

        # Add files as edges
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                file_node = graph.add_node(file_path, file_size, file_size)
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

    return graph, total_capacity

# Main function to run knapsack with graph and dynamic capacity
def run_knapsack_with_dynamic_graph(root_directory):
    # Traverse the directory and insert data into the graph
    graph, total_capacity = insert_in_graph(root_directory)

    # Retrieve weights and values from the graph
    weights, values, dynamic_capacity = graph.traverse_graph()

    # Apply the knapsack algorithm with the dynamically calculated total capacity
    max_value = knapsack(values, weights, dynamic_capacity)
    print(f"Maximum value achievable without exceeding dynamic capacity: {max_value}")

# Example usage for knapsack with graph
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_knapsack_with_dynamic_graph(root_directory)
