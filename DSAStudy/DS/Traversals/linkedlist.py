import os
import time
import sys

# Linked List implementation for storing paths
class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data  # Store the path (data) in the node
            self.next = None  # Pointer to the next node

    def __init__(self):
        self.head = None  # Initialize the head of the linked list
        self.size = 0  # Track the number of nodes for space complexity

    # Insert a new path (node) into the linked list
    def insert(self, data):
        new_node = self.Node(data)  # Create a new node with the given path
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update the head to be the new node
        self.size += 1  # Increment the size of the linked list

    # Traverse the linked list (simulate operation)
    def traverse_and_apply_operations(self):
        current = self.head
        while current is not None:
            # Simulate an operation (here we just print, but you can apply real algorithms)
            # print(f"Processing path: {current.data}")
            current = current.next

# Collect all paths in the directory into a linked list
def collect_paths_into_linked_list(root_directory):
    linked_list = LinkedList()
    
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Insert directory path into the linked list
        linked_list.insert(dirpath)
        
        # Insert each file path in the directory into the linked list
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            linked_list.insert(file_path)
    
    return linked_list

# Function to perform operations and measure time and space complexity
def perform_operations_on_linked_list(linked_list):
    # Measure space complexity (size of the linked list in bytes)
    space_used = sys.getsizeof(linked_list) + linked_list.size * sys.getsizeof(LinkedList.Node(None))
    
    # Time complexity: Measure time to traverse the entire linked list
    start_time = time.time()
    linked_list.traverse_and_apply_operations()  # Traverse and apply operations
    end_time = time.time()

    time_taken = end_time - start_time
    
    # Output for Excel in the format you requested
    print(f"Directory Traversal, O(n), O(n), {time_taken:.6f} seconds, {space_used} bytes")

# Main function
def main():
    # Define the root directory (adjust this to your actual directory path)
    root_directory = "/Volumes/CD/pCLE"
    
    # Step 1: Collect all paths into the linked list
    linked_list = collect_paths_into_linked_list(root_directory)
    
    # Step 2: Perform operations on the linked list and measure complexities
    perform_operations_on_linked_list(linked_list)

# Run the main function
if __name__ == "__main__":
    main()
