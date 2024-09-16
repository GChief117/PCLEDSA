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

    # Split the linked list into two halves
    def split(self, head):
        if not head or not head.next:
            return head, None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        return head, middle

    # Merge two sorted linked lists
    def merge(self, left, right):
        dummy = Node(None)
        tail = dummy
        while left and right:
            if left.data < right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left or right
        return dummy.next

    # MergeSort function for linked list
    def merge_sort(self, head):
        if not head or not head.next:
            return head
        left, right = self.split(head)
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        return self.merge(left, right)

    # Apply MergeSort to the linked list and measure complexities
    def merge_sort_directory(self):
        # Measure space complexity
        space_used = sys.getsizeof(self)
        print(f"Space complexity: {space_used} bytes (for the linked list)")

        # Measure time taken to sort the linked list
        start_time = time.time()
        self.head = self.merge_sort(self.head)
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply MergeSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Output sorted list
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
            file_path = os.path.join(dirpath, filename)
            linked_list.append(file_path)
    return linked_list

# Example usage:
root_directory = "/Volumes/CD/pCLE"  # Replace with your root directory path
linked_list = collect_paths_linked_list(root_directory)
linked_list.merge_sort_directory()
