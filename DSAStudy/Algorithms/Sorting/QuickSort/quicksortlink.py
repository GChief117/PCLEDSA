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

    # Add node to the front of the list
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Partition for quicksort
    def partition(self, head):
        if not head or not head.next:
            return head, None

        pivot = head
        prev = head
        curr = head.next

        while curr:
            if curr.data < pivot.data:
                prev = prev.next
                prev.data, curr.data = curr.data, prev.data
            curr = curr.next

        head.data, prev.data = prev.data, head.data
        return prev, prev.next

    # QuickSort implementation for Linked List
    def quicksort(self, head):
        if not head or not head.next:
            return head

        pivot, next_part = self.partition(head)
        left_head = self.quicksort(head)
        right_head = self.quicksort(next_part)

        return self.concatenate(left_head, pivot, right_head)

    # Concatenate partitions
    def concatenate(self, left, pivot, right):
        if left:
            curr = left
            while curr.next:
                curr = curr.next
            curr.next = pivot
        else:
            left = pivot

        pivot.next = right
        return left

    # Apply quicksort and measure space and time complexity
    def quicksort_linked_list(self):
        # Measure space complexity
        space_used = sys.getsizeof(self)
        print(f"Space complexity: {space_used} bytes (for the linked list)")

        # Measure time taken to sort the linked list
        start_time = time.time()
        self.head = self.quicksort(self.head)
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply QuickSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Output sorted list
        current = self.head
        while current:
            print(f"Processing path: {current.data}")
            current = current.next

# Example usage:
linked_list = LinkedList()
linked_list.insert("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL001.txt")
linked_list.insert("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt")
linked_list.insert("/Volumes/CD/pCLE/Dye_Concentration_Experiments/CanineTissue/liver_cancer/CAN001.txt")

linked_list.quicksort_linked_list()
