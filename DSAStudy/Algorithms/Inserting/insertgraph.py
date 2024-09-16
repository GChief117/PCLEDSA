import os
import sys
import time

class GraphNode:
    def __init__(self, file_path, file_size):
        self.file_path = file_path
        self.file_size = file_size
        self.adjacent = []

    def add_neighbor(self, neighbor_node):
        self.adjacent.append(neighbor_node)

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, file_path, file_size):
        new_node = GraphNode(file_path, file_size)
        self.nodes[file_path] = new_node
        return new_node

    def add_edge(self, from_node, to_node):
        from_node.add_neighbor(to_node)

# Function to insert a file into a graph (simulating file insertion)
def insert_file_into_graph(graph, file_path):
    try:
        file_size = os.path.getsize(file_path)
    except OSError:
        print(f"Error retrieving file size for {file_path}")
        return

    # Start timing the insertion
    start_time = time.time()

    # Add the new file as a node in the graph
    graph.add_node(file_path, file_size)

    end_time = time.time()
    print(f"Time taken for graph file insertion: {end_time - start_time:.6f} seconds")
    print(f"Time complexity: O(1)")

# Function to traverse the directory and collect files using graph
def traverse_directory_for_graph(root_directory):
    graph = Graph()
    parent_map = {}

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        parent_node = graph.add_node(dirpath, len(dirpath))  # Add directory as a node
        parent_map[dirpath] = parent_node

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                file_node = graph.add_node(file_path, file_size)  # Add file as a node
                graph.add_edge(parent_map[dirpath], file_node)
            except OSError:
                continue

    end_time = time.time()
    print(f"Time taken for directory traversal: {end_time - start_time:.6f} seconds")

    # Measure space complexity for graph
    space_used_graph = sys.getsizeof(graph)
    print(f"Space complexity for graph: {space_used_graph} bytes")

    return graph

# Main function to perform file insertion into graph
def run_file_insertion_with_graph(root_directory, file_to_insert):
    # Traverse the directory and collect files
    graph = traverse_directory_for_graph(root_directory)

    # Insert the new file into the graph
    print(f"\nInserting {file_to_insert} into the graph:")
    insert_file_into_graph(graph, file_to_insert)

# Example usage for graph file insertion
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    file_to_insert = "/path/to/new/file.txt"  # Replace with the path of the new file
    run_file_insertion_with_graph(root_directory, file_to_insert)
