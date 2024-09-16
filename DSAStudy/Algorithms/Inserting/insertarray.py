import sys
import time

# Insert a new path into the array (representing directories/files)
def insert_in_array(paths, index, new_path):
    start_time = time.time()  # Start the timer
    paths = paths[:index] + [new_path] + paths[index:]  # Insert by slicing
    end_time = time.time()  # End the timer

    # Measure space complexity
    space_used = sys.getsizeof(paths)
    print(f"Space complexity: {space_used} bytes (for the array)")

    # Measure time complexity
    time_taken = end_time - start_time
    print(f"Time taken to insert into array: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n)")

    # Output modified array
    for path in paths:
        print(f"Inserted path: {path}")

    return paths

# Example usage for the root directory array
root_directory = [
    "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL001.txt",
    "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt"
]

new_path = "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL003.txt"
insert_in_array(root_directory, 1, new_path)
