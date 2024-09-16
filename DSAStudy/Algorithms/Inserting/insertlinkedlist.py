import os
import sys
import time

class Node:
    def __init__(self, file_path, file_size):
        self.file_path = file_path
        self.file_size = file_size
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, file_path, file_size):
        new_node = Node(file_path, file_size)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

# Function to insert a file into a linked list (simulating file insertion)
def insert_file_into_linked_list(linked_list, file_path):
    try:
        file_size = os.path.getsize(file_path)
    except OSError:
        print(f"Error retrieving file size for {file_path}")
        return
    
    # Start timing the insertion
    start_time = time.time()

    linked_list.insert(file_path, file_size)

    end_time = time.time()
    print(f"Time taken for linked list file insertion: {end_time - start_time:.6f} seconds")
    print(f"Time complexity: O(n)")

# Function to traverse the directory and collect files using linked list
def traverse_directory_for_linked_list(root_directory):
    linked_list = LinkedList()

    # Start timing the traversal
    start_time = time.time()

    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                linked_list.insert(file_path, file_size)
            except OSError:
                continue

    end_time = time.time()
    print(f"Time taken for directory traversal: {end_time - start_time:.6f} seconds")

    # Measure space complexity for linked list
    space_used_list = sys.getsizeof(linked_list)
    print(f"Space complexity for linked list: {space_used_list} bytes")

    return linked_list

# Main function to perform file insertion into linked list
def run_file_insertion_with_linked_list(root_directory, file_to_insert):
    # Traverse the directory and collect files
    linked_list = traverse_directory_for_linked_list(root_directory)

    # Insert the new file into the linked list
    print(f"\nInserting {file_to_insert} into the linked list:")
    insert_file_into_linked_list(linked_list, file_to_insert)

# Example usage for linked list file insertion
if __name__ == "__main__":
    root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
    file_to_insert = "/path/to/new/file.txt"  # Replace with the path of the new file
    run_file_insertion_with_linked_list(root_directory, file_to_insert)
