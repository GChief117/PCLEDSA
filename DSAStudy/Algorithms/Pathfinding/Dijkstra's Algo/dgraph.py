import os
import sys
import heapq
import time

# Dijkstra's Algorithm to find shortest paths in a graph
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Build a graph from the root directory, where directories and files are nodes, and we assign weights to edges
def build_graph_from_directory(root_directory):
    graph = {}
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Each directory and file is a node
        if dirpath not in graph:
            graph[dirpath] = []

        # Add edges between the current directory and subdirectories/files with some weight (e.g., 1)
        for dirname in dirnames:
            full_dir_path = os.path.join(dirpath, dirname)
            graph[dirpath].append((full_dir_path, 1))
            if full_dir_path not in graph:
                graph[full_dir_path] = []
        
        for filename in filenames:
            full_file_path = os.path.join(dirpath, filename)
            graph[dirpath].append((full_file_path, 1))
            if full_file_path not in graph:
                graph[full_file_path] = []

    return graph

# Apply Dijkstra's Algorithm to the root directory graph and measure space and time complexity
def apply_dijkstra_directory_graph(root_directory, start_node):
    graph = build_graph_from_directory(root_directory)

    # Measure space complexity
    space_used = sys.getsizeof(graph)
    print(f"Space complexity: {space_used} bytes (for the graph)")

    # Measure time complexity (time taken to run Dijkstra's Algorithm)
    start_time = time.time()
    distances = dijkstra(graph, start_node)
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to run Dijkstra's Algorithm: {time_taken:.6f} seconds")
    print(f"Time complexity: O((V + E) log V) where V is the number of directories/files and E is the number of connections")

    # Output the shortest distances from the start node to each node
    for node, distance in distances.items():
        print(f"Distance from {start_node} to {node}: {distance}")

# Example usage for the root directory graph
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory
start_node = "/Volumes/CD/pCLE"  # The starting directory node
apply_dijkstra_directory_graph(root_directory, start_node)
