import os
import sys
import time

class Graph:
    def __init__(self):
        self.graph = {}

    # Add a node (directory or file) to the graph
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    # Add an edge between two nodes (file to directory, or subdirectory to directory)
    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append(node2)

# Insert directories and files into a graph while calculating Fibonacci
def insert_in_graph_fib(root_directory):
    graph = Graph()
    memo = {}

    # Traverse the directory structure
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Add directory as a node
        graph.add_node(dirpath)
        
        # Add edges and calculate Fibonacci for subdirectories
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            graph.add_edge(dirpath, subdir_path)
            fib_result = fibonacci_memo(len(subdir_path), memo)
            print(f"Fibonacci({len(subdir_path)}) result for subdirectory: {subdir_path} = {fib_result}")

        # Add edges and calculate Fibonacci for files
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            graph.add_edge(dirpath, file_path)
            fib_result = fibonacci_memo(len(file_path), memo)
            print(f"Fibonacci({len(file_path)}) result for file: {file_path} = {fib_result}")

    # Measure space complexity (space used by the graph)
    space_used = sys.getsizeof(graph.graph)
    print(f"Space complexity: {space_used} bytes (for the graph)")

    # Measure time complexity for processing the graph
    start_time = time.time()
    for node in graph.graph:
        fibonacci_memo(len(node), memo)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to process graph: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n)")

    # Print the graph structure
    print("\n--- Graph Structure ---")
    for node, edges in graph.graph.items():
        print(f"Node: {node}")
        for edge in edges:
            print(f"  -> {edge}")

# Example usage for the graph
root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
insert_in_graph_fib(root_directory)
