import time
import sys
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Add edges between nodes (paths)
    def add_edge(self, node, neighbor):
        self.graph[node].append(neighbor)

    # QuickSort nodes and neighbors in the graph
    def quicksort_graph(self):
        # Convert the graph's nodes and neighbors into arrays
        node_arr = list(self.graph.keys())
        
        # Measure space complexity
        space_used = sys.getsizeof(self.graph)
        print(f"Space complexity: {space_used} bytes (for the graph)")

        # Sort nodes using QuickSort
        start_time = time.time()
        sorted_nodes = quicksort(node_arr)  # Sort nodes
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply QuickSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Output sorted nodes
        for node in sorted_nodes:
            print(f"Processing path: {node}")

# QuickSort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage:
graph = Graph()
graph.add_edge("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon", "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL001.txt")
graph.add_edge("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon", "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt")
graph.add_edge("/Volumes/CD/pCLE/Dye_Concentration_Experiments/CanineTissue/liver_cancer", "/Volumes/CD/pCLE/Dye_Concentration_Experiments/CanineTissue/liver_cancer/CAN001.txt")

graph.quicksort_graph()
