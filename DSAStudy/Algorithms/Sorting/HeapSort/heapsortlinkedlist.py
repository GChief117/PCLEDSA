import os
import time
import sys

# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Convert the linked list into an array
    def to_array(self):
        array = []
        current = self.head
        while current:
            array.append(current.data)
            current = current.next
        return array

    # Convert an array back into a linked list
    def from_array(self, array):
        self.head = None
        for item in array:
            self.append(item)

    # HeapSort the linked list
    def heap_sort_linked_list(self):
        # Convert linked list to array
        array = self.to_array()

        # Measure space complexity
        space_used = sys.getsizeof(array)
        print(f"Space complexity: {space_used} bytes (for the linked list)")

        # Measure time taken to apply HeapSort
        start_time = time.time()
        sorted_array = heap_sort(array)
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply HeapSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Convert the sorted array back into a linked list
        self.from_array(sorted_array)

        # Output sorted linked list
        current = self.head
        while current:
            print(f"Processing path: {current.data}")
            current = current.next

# Collect all paths in the directory into a linked list
def collect_paths_linked_list(root_directory):
    linked_list = LinkedList()
    for dirpath, dirnames, filenames in os.walk(root_directory):
        linked_list.append(dirpath)
        for filename in filenames:
            linked_list.append(os.path.join(dirpath, filename))
    return linked_list

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory path
linked_list = collect_paths_linked_list(root_directory)
linked_list.heap_sort_linked_list()
