import os
import sys
import time

# Graph node class
class GraphNode:
    def __init__(self, data):
        self.data = data
        self.adjacent = []  # Stores connections to other nodes

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

    def collect_file_sizes(self):
        file_sizes = []
        for node in self.nodes.values():
            file_sizes.append(node.data)
        return file_sizes

# Karatsuba multiplication function
def karatsuba(x, y):
    # Start timing the Karatsuba multiplication
    start_time = time.time()

    if x < 10 or y < 10:
        result = x * y
    else:
        m = min(len(str(x)), len(str(y)))
        m2 = m // 2

        high1, low1 = divmod(x, 10**m2)
        high2, low2 = divmod(y, 10**m2)

        z0 = karatsuba(low1, low2)
        z1 = karatsuba((low1 + high1), (low2 + high2))
        z2 = karatsuba(high1, high2)

        result = (z2 * 10**(2 * m2)) + ((z1 - z2 - z0) * 10**m2) + z0

    end_time = time.time()
    print(f"Time taken for Karatsuba multiplication: {end_time - start_time:.6f} seconds")
    print(f"Time complexity: O(n^1.585)")
    return result

# Function to traverse the directory and collect file sizes using a graph
def traverse_directory_for_graph(root_directory):
    graph = Graph()

    # Start timing the traversal
    start_time = time.time()

    parent_map = {}
    for dirpath, dirnames, filenames in os.walk(root_directory):
        if dirpath not in graph.nodes:
            parent_map[dirpath] = graph.add_node(len(dirpath))

        # Add subdirectories and files as graph nodes
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            subdir_node = graph.add_node(len(subdir_path))
            graph.add_edge(parent_map[dirpath], subdir_node)
            parent_map[subdir_path] = subdir_node

        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                file_node = graph.add_node(file_size)
                graph.add_edge(parent_map[dirpath], file_node)
            except OSError:
                continue

    end_time = time.time()
    print(f"Time taken for directory traversal: {end_time - start_time:.6f} seconds")

    # Measure space complexity for the graph
    space_used = sys.getsizeof(graph)
    print(f"Space complexity for graph: {space_used} bytes")

    return graph

# Main function to run Karatsuba algorithm with graph
def run_karatsuba_with_graph(root_directory):
    # Traverse the directory and collect file sizes
    graph = traverse_directory_for_graph(root_directory)
    file_sizes = graph.collect_file_sizes()

    # Select two largest file sizes for Karatsuba multiplication
    if len(file_sizes) >= 2:
        x, y = sorted(file_sizes)[-2:]
        print(f"Multiplying {x} and {y} using Karatsuba Algorithm")
        result = karatsuba(x, y)
        print(f"Result of Karatsuba multiplication: {result}")
    else:
        print("Not enough files to perform Karatsuba multiplication")

# Example usage for Karatsuba algorithm with graph
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_karatsuba_with_graph(root_directory)
