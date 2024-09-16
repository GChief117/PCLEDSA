import os
import sys
import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

# Binary search function for linked list (converted to sorted list)
def binary_search(sorted_weights):
    low, high = 0, len(sorted_weights) - 1

    # Start timing the binary search
    start_time = time.time()

    while low <= high:
        mid = (low + high) // 2
        print(f"Processing file size at index {mid}: {sorted_weights[mid]} bytes")
        low = mid + 1

    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to perform binary search: {time_taken:.6f} seconds")
    print(f"Time complexity: O(log n), where n = {len(sorted_weights)}")

# Function to traverse the directory and insert into a linked list
def traverse_directory_for_linked_list(root_directory):
    linked_list = LinkedList()

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                linked_list.insert(file_size)
            except OSError:
                continue

    end_time = time.time()
    time_taken = end_time - start_time

    # Measure space complexity for storing linked list
    space_used_list = sys.getsizeof(linked_list)
    print(f"Space complexity for linked list: {space_used_list} bytes")
    print(f"Time taken for directory traversal: {time_taken:.6f} seconds")

    return linked_list

# Main function for binary search with linked list
def run_binary_search_with_linked_list(root_directory):
    # Traverse the directory and collect file sizes
    linked_list = traverse_directory_for_linked_list(root_directory)

    # Convert linked list to a sorted list
    sorted_weights = sorted(linked_list.to_list())

    # Perform binary search
    binary_search(sorted_weights)

# Example usage for binary search with linked list
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    run_binary_search_with_linked_list(root_directory)
