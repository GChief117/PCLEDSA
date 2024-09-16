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

# Insert directories into a linked list while calculating Fibonacci for each path
def insert_in_linked_list_fib(root_directory):
    linked_list = LinkedList()
    memo = {}

    for dirpath, dirnames, filenames in os.walk(root_directory):
        linked_list.insert_at_end(dirpath)  # Insert directory path into the linked list
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            linked_list.insert_at_end(file_path)  # Insert file path into the linked list

            # Calculate Fibonacci for the current path length using memoization
            fib_result = fibonacci_memo(len(file_path), memo)
            print(f"Fibonacci({len(file_path)}) result for file: {file_path} = {fib_result}")

    # Measure space complexity (space used by the linked list)
    space_used = sys.getsizeof(linked_list)
    print(f"Space complexity: {space_used} bytes (for the linked list)")

    # Measure time complexity
    start_time = time.time()
    current = linked_list.head
    while current:
        fibonacci_memo(len(current.data), memo)
        current = current.next
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to process linked list: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n)")

# Example usage for the linked list
insert_in_linked_list_fib(root_directory)
