import os
import time
import sys
from collections import defaultdict, deque

# Graph implementation using an adjacency list
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Initialize an empty adjacency list

    # Add an edge between a directory and its contents (subdirectories/files)
    def add_edge(self, node, neighbor):
        self.graph[node].append(neighbor)

    # Breadth-First Search (BFS) to traverse the graph
    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    # Depth-First Search (DFS) to traverse the graph
    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()

        if node not in visited:
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited)

# Collect all paths in the directory into a graph
def collect_paths_into_graph(root_directory):
    graph = Graph()
    
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Add edges between directory and its subdirectories
        for dirname in dirnames:
            subdir_path = os.path.join(dirpath, dirname)
            graph.add_edge(dirpath, subdir_path)

        # Add edges between directory and its files
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            graph.add_edge(dirpath, file_path)
    
    return graph

# Function to perform operations and measure time and space complexity
def perform_operations_on_graph(graph, start_node):
    # Measure space complexity
    space_used = sys.getsizeof(graph.graph) + sum(sys.getsizeof(v) for v in graph.graph.values())
    
    # Store results for formatted output
    results = []

    # Time complexity: Measure time to perform BFS traversal
    start_time = time.time()
    graph.bfs(start_node)
    end_time = time.time()
    time_taken_bfs = end_time - start_time
    results.append(["BFS Traversal", "O(V + E)", "O(V + E)", f"{time_taken_bfs:.6f} seconds", f"{space_used} bytes"])

    # Time complexity: Measure time to perform DFS traversal
    start_time = time.time()
    graph.dfs(start_node)
    end_time = time.time()
    time_taken_dfs = end_time - start_time
    results.append(["DFS Traversal", "O(V + E)", "O(V + E)", f"{time_taken_dfs:.6f} seconds", f"{space_used} bytes"])

    # Print the results in the required format
    print(f"{'Operation':<25} {'Time Complexity':<15} {'Space Complexity':<15} {'Time (in seconds)':<20} {'Size (in bytes)':<15}")
    for result in results:
        print(f"{result[0]:<25} {result[1]:<15} {result[2]:<15} {result[3]:<20} {result[4]:<15}")

# Main function
def main():
    # Define the root directory (adjust this to your actual directory path)
    root_directory = "/Volumes/CD/pCLE"
    
    # Step 1: Collect all paths into the graph
    graph = collect_paths_into_graph(root_directory)
    
    # Step 2: Perform operations on the graph and measure complexities
    start_node = root_directory  # Start traversal from the root directory
    perform_operations_on_graph(graph, start_node)

# Run the main function
if __name__ == "__main__":
    main()
