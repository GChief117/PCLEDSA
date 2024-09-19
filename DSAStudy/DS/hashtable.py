import os
import time
import sys

# HashTable implementation for storing paths
class HashTable:
    def __init__(self):
        self.table = {}  # Using a Python dictionary to implement a hash table

    # Insert a new path into the hash table
    def insert(self, key, data):
        self.table[key] = data  # Use the path as the key and store data

    # Retrieve a path from the hash table
    def retrieve(self, key):
        return self.table.get(key, None)  # Return the data if the key exists, else None

    # Traverse the hash table (process all paths)
    def traverse_and_apply_operations(self):
        for key, value in self.table.items():
            # Simulate an operation (here we just traverse and apply)
            pass

# Collect all paths in the directory into a hash table
def collect_paths_into_hashtable(root_directory):
    hashtable = HashTable()
    
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # Insert directory path into the hash table
        hashtable.insert(dirpath, dirpath)
        
        # Insert each file path in the directory into the hash table
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            hashtable.insert(file_path, file_path)
    
    return hashtable

# Function to perform operations and measure time and space complexity
def perform_operations_on_hashtable(hashtable):
    # Measure space complexity (size of the hash table in bytes)
    space_used = sys.getsizeof(hashtable.table) + sum([sys.getsizeof(k) + sys.getsizeof(v) for k, v in hashtable.table.items()])
    
    # Time complexity: Measure time to traverse the entire hash table
    start_time = time.time()
    hashtable.traverse_and_apply_operations()  # Traverse and apply operations
    end_time = time.time()

    time_taken = end_time - start_time
    
    # Output the results in the format you need for Excel
    print(f"Directory Traversal, O(1) on average, O(n), {time_taken:.6f} seconds, {space_used} bytes")

# Main function
def main():
    # Define the root directory (adjust this to your actual directory path)
    root_directory = "/Volumes/CD/pCLE"
    
    # Step 1: Collect all paths into the hash table
    hashtable = collect_paths_into_hashtable(root_directory)
    
    # Step 2: Perform operations on the hash table and measure complexities
    perform_operations_on_hashtable(hashtable)

# Run the main function
if __name__ == "__main__":
    main()
