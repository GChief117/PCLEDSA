//
//  main.cpp
//  Queue
//
//  Created by Gunnar Beck on 9/19/24.
//

#include <iostream>
#include <deque>
#include <filesystem>
#include <chrono>

using namespace std;
using namespace filesystem;
using namespace chrono;

// Queue class to store paths using deque (FIFO)
class Queue {
public:
    deque<string> queue;  // Deque to simulate queue behavior

    // Enqueue a new path into the queue
    void enqueue(const string& data) {
        queue.push_back(data);  // Add path to the end of the queue
    }

    // Dequeue a path from the queue (FIFO)
    string dequeue() {
        if (!is_empty()) {
            string front = queue.front();  // Get the front element
            queue.pop_front();             // Remove it from the queue
            return front;
        }
        return "";
    }

    // Check if the queue is empty
    bool is_empty() const {
        return queue.empty();
    }

    // Traverse the queue (process each path from front to back)
    void traverse_and_apply_operations() {
        while (!is_empty()) {
            string path = dequeue();  // Dequeue the front path
            // Simulate an operation (you can add specific operations here)
            // cout << "Processing path: " << path << endl;  // Uncomment to print paths
        }
    }
};

// Collect all paths in the directory into a queue
Queue collect_paths_into_queue(const string& root_directory) {
    Queue queue;
    
    for (const auto& entry : recursive_directory_iterator(root_directory)) {
        // Enqueue each path into the queue
        queue.enqueue(entry.path().string());
    }
    
    return queue;
}

// Perform operations on the queue and measure time and space complexity
void perform_operations_on_queue(Queue& queue) {
    // Measure space complexity (approximation)
    size_t space_used = sizeof(queue) + queue.queue.size() * sizeof(string);

    // Time the traversal
    auto start_time = high_resolution_clock::now();
    queue.traverse_and_apply_operations();  // Traverse and apply operations
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

    // Step 1: Collect all paths into the queue
    Queue queue = collect_paths_into_queue(root_directory);

    // Step 2: Perform operations on the queue and measure complexities
    perform_operations_on_queue(queue);

    return 0;
}
