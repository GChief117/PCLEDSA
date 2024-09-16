import time
import sys

# QuickSort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Measure space and time complexity for QuickSort on arrays
def quicksort_array(arr):
    # Measure space complexity before sorting
    space_used = sys.getsizeof(arr)
    print(f"Space complexity: {space_used} bytes (for the array)")

    # Measure time taken to sort the array
    start_time = time.time()
    sorted_arr = quicksort(arr)
    end_time = time.time()
    
    time_taken = end_time - start_time
    print(f"Time taken to apply QuickSort: {time_taken:.6f} seconds")
    print(f"Time complexity: O(n log n)")

    # Output sorted array as "processing paths"
    for path in sorted_arr:
        print(f"Processing path: {path}")

# Example usage:
arr = ["/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL001.txt",
       "/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt",
       "/Volumes/CD/pCLE/Dye_Concentration_Experiments/CanineTissue/liver_cancer/CAN001.txt"]

quicksort_array(arr)
