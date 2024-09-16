import os
import sys
import time

# Linked List Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Add node to the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Convert linked list to array for binary search
    def to_array(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr

# Apply binary search on a linked list
def apply_binary_search_linked_list(root_directory, target):
    llist = LinkedList()

    # Step 1: Collect paths and insert into linked list
    for dirpath, dirnames, filenames in os.walk(root_directory):
        llist.append(dirpath)
        for filename in filenames:
            llist.append(os.path.join(dirpath, filename))

    # Step 2: Convert linked list to array and sort it
    paths = llist.to_array()
    paths.sort()

    # Measure space complexity
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes (for the linked list)")

    # Measure time complexity
    start_time = time.time()
    index = binary_search(paths, target)
    end_time = time.time()

    time_taken = end_time - start_time
    print(f"Time taken to perform binary search: {time_taken:.6f} seconds")
    print(f"Time complexity: O(log n)")

    if index != -1:
        print(f"Target found at index {index}: {paths[index]}")
    else:
        print("Target not found")

# Example usage for linked lists
root_directory = "/Volumes/CD/pCLE"
target = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
apply_binary_search_linked_list(root_directory, target)
