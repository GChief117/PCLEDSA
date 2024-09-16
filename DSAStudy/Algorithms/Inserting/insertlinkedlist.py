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
        start_time = time.time()  # Start the timer
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        end_time = time.time()  # End the timer

        # Measure space complexity
        space_used = sys.getsizeof(new_node)
        print(f"Space complexity: {space_used} bytes (for the new node)")

        # Measure time complexity
        time_taken = end_time - start_time
        print(f"Time taken to insert into linked list: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n)")

    def display(self):
        current = self.head
        while current:
            print(f"Inserted path: {current.data}")
            current = current.next

# Example usage for the linked list
linked_list = LinkedList()
linked_list.insert_at_end("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL001.txt")
linked_list.insert_at_end("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt")
linked_list.insert_at_end("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL003.txt")
linked_list.display()
