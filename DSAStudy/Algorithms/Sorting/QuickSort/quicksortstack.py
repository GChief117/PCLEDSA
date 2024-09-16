import time
import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    # QuickSort the stack
    def quicksort_stack(self):
        # Convert stack to array
        arr = self.stack.copy()  # Convert to array for sorting

        # Measure space complexity
        space_used = sys.getsizeof(self.stack)
        print(f"Space complexity: {space_used} bytes (for the stack)")

        # Measure time taken to apply QuickSort
        start_time = time.time()
        sorted_arr = quicksort(arr)  # Use QuickSort function from earlier
        end_time = time.time()

        time_taken = end_time - start_time
        print(f"Time taken to apply QuickSort: {time_taken:.6f} seconds")
        print(f"Time complexity: O(n log n)")

        # Push sorted elements back into the stack
        self.stack = sorted_arr

        # Output sorted stack
        for item in self.stack:
            print(f"Processing path: {item}")

# QuickSort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage:
stack = Stack()
stack.push("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL001.txt")
stack.push("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt")
stack.push("/Volumes/CD/pCLE/Dye_Concentration_Experiments/CanineTissue/liver_cancer/CAN001.txt")

stack.quicksort_stack()
