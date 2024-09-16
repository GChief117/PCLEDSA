import os
import sys
import time

# Insert directories into an array while calculating Fibonacci for each path
def insert_in_array_fib(root_directory):
    paths = []
    memo = {}

    for dirpath, dirnames, filenames in os.walk(root_directory):
        paths.append(dirpath)  # Insert directory path into the array
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            paths.append(file_path)  # Insert file path into the array

            # Calculate Fibonacci for the current path length using memoization
            fib_result = fibonacci_memo(len(file_path), memo)
            print(f"Fibonacci({len(file_path)}) result for file: {file_path} = {fib_result}")

    # Measure space complexity (space used by the array)
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes (for the array)")

    # Measure time complexity for Fibonacci processing
    start_time = time.time()
    for path in paths:
        fibonacci_memo(len(path), memo)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time taken to process array: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n)")

# Example usage for the array
root_directory = "/Volumes/CD/pCLE"  # Replace with your actual root directory
insert_in_array_fib(root_directory)
