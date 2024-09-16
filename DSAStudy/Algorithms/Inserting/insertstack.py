import sys
import time

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        start_time = time.time()  # Start the timer
        self.stack.append(data)
        end_time = time.time()  # End the timer

        # Measure space complexity
        space_used = sys.getsizeof(self.stack)
        print(f"Space complexity: {space_used} bytes (for the stack)")

        # Measure time complexity
        time_taken = end_time - start_time
        print(f"Time taken to push into stack: {time_taken:.6f} seconds")
        print(f"Time complexity: O(1)")

    def display(self):
        for item in self.stack:
            print(f"Stack path: {item}")

# Example usage for the stack
stack = Stack()
stack.push("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL001.txt")
stack.push("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL002.txt")
stack.push("/Volumes/CD/pCLE/Dye_Concentration_Experiments/BovineTissue/Colon/COL003.txt")
stack.display()
