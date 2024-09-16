import time
import sys

# Tree Node class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    # Add child node to the tree
    def add_child(self, child_node):
        self.children.append(child_node)

# General Tree class
class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    # Flatten the tree into a list using pre-order traversal
    def flatten_tree(self, node, result=None):
        if result is None:
            result = []
        result.append(node.data)
        for child in node.children:
            self.flatten_tree(child, result)
        return result

    # Rebuild the tree from sorted list (for demonstration purposes)
    def rebuild_tree(self, sorted_data):
        # Simple rebuilding where sorted nodes are children of root
        self.root.children = [TreeNode(data) for data in sorted_data]

    # QuickSort the tree by flattening, sorting, and rebuilding
    def quicksort_tree(self):
        # Step 1: Flatten the tree into a list
        flattened_tree = self.flatten_tree(self.root)

        # Measure space complexity
        space_used = sys.getsizeof(flattened_tree)
        print(f"Space complexity: {space_used} bytes (for the flattened tree)")

        # Step 2: Sort the flattened list using QuickSort
        start_time = time.time()
        sorted_tree = quicksort(flattened_tree)  # QuickSort function
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply QuickSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Step 3: Rebuild the tree based on the sorted result
        self.rebuild_tree(sorted_tree)

        # Output sorted tree
        for node in sorted_tree:
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
tree = Tree("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon")
tree.root.add_child(TreeNode("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL001.txt"))
tree.root.add_child(TreeNode("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"))
tree.root.add_child(TreeNode("/Volumes/CD/pCLE/Dye_Concentration_Experiments/CanineTissue/liver_cancer/CAN001.txt"))

tree.quicksort_tree()
