//
//  main.cpp
//  Stack
//
//  Created by Gunnar Beck on 9/19/24.
//

#include <iostream>
#include <vector>
#include <filesystem>
#include <chrono>

using namespace std;
using namespace filesystem;
using namespace chrono;

// Stack class to store paths using vector (LIFO)
class Stack {
public:
    vector<string> stack;  // Vector to simulate stack behavior

    // Push a new path onto the stack
    void push(const string& data) {
        stack.push_back(data);  // Add a path to the top of the stack
    }

    // Pop a path off the stack (LIFO)
    string pop() {
        if (!is_empty()) {
            string top = stack.back();  // Get the top element
            stack.pop_back();           // Remove it from the stack
            return top;
        }
        return "";
    }

    // Check if the stack is empty
    bool is_empty() const {
        return stack.empty();
    }

    // Traverse the stack (process each path from top to bottom)
    void traverse_and_apply_operations() {
        while (!is_empty()) {
            string path = pop();  // Pop the top path from the stack
            // Simulate an operation (you can add specific operations here)
            // cout << "Processing path: " << path << endl;  // Uncomment to print paths
        }
    }
};

// Collect all paths in the directory into a stack
Stack collect_paths_into_stack(const string& root_directory) {
    Stack stack;
    
    for (const auto& entry : recursive_directory_iterator(root_directory)) {
        // Push each path onto the stack
        stack.push(entry.path().string());
    }
    
    return stack;
}

// Perform operations on the stack and measure time and space complexity
void perform_operations_on_stack(Stack& stack) {
    // Measure space complexity (approximation)
    size_t space_used = sizeof(stack) + stack.stack.capacity() * sizeof(string);  // Approximate size

    // Time the traversal
    auto start_time = high_resolution_clock::now();
    stack.traverse_and_apply_operations();  // Traverse and apply operations
    auto end_time = high_resolution_clock::now();
    
    duration<double> time_taken = end_time - start_time;

    // Output the results for Excel
    cout << "Directory Traversal, O(n), O(n), "
         << time_taken.count() << " seconds, " << space_used << " bytes" << endl;
}

// Main function
int main() {
    // Define the root directory (adjust this to your actual directory path)
    string root_directory = "/Volumes/CD/pCLE";  // Adjust the path as needed

    // Step 1: Collect all paths into the stack
    Stack stack = collect_paths_into_stack(root_directory);

    // Step 2: Perform operations on the stack and measure complexities
    perform_operations_on_stack(stack);

    return 0;
}
