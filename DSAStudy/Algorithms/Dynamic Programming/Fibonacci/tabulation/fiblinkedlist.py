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

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

# Insert directories and files into a linked list while calculating Fibonacci using tabulation
def insert_in_linked_list_fib_tab(root_directory):
    linked_list = LinkedList()

    # Traverse the directory structure
    for dirpath, dirnames, filenames in os.walk(root_directory):
        linked_list.insert_at_end(dirpath)  # Insert directory path into the linked list
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            linked_list.insert_at_end(file_path)  # Insert file path into the linked list

            # Calculate Fibonacci for the current path length using tabulation
            fib_result = fibonacci_tab(len(file_path))
            print(f"Fibonacci({len(file_path)}) result for file: {file_path} = {fib_result}")

    # Measure space complexity (space used by the linked list)
    space_used = sys.getsizeof(linked_list)
    print(f"Space complexity: {space_used} bytes (for the linked list)")

    # Measure time complexity
    start_time = time.time()
    current = linked_list.head
    while current:
        fibonacci_tab(len(current.data))
        current = current.next
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to process linked list: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n)")

# Example usage for the linked list with tabulation
root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
insert_in_linked_list_fib_tab(root_directory)
