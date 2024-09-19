//
//  main.cpp
//  LinkedList
//
//  Created by Gunnar Beck on 9/19/24.
//

#include <iostream>
#include <filesystem>
#include <chrono>
#include <string>

using namespace std;
using namespace filesystem;
using namespace chrono;

// Node structure for Linked List
struct Node {
    string data;  // Store the path as data
    Node* next;   // Pointer to the next node

    Node(string path) : data(path), next(nullptr) {}
};

// Linked List structure for storing paths
class LinkedList {
public:
    Node* head;
    int size;  // Track the size of the linked list

    LinkedList() : head(nullptr), size(0) {}

    // Insert a new path at the beginning of the linked list
    void insert(const string& path) {
        Node* new_node = new Node(path);  // Create a new node
        new_node->next = head;            // Point the new node to the current head
        head = new_node;                  // Update the head to the new node
        size++;                           // Increment size
    }

    // Traverse the linked list (simulate an operation)
    void traverse_and_apply_operations() const {
        Node* current = head;
        while (current != nullptr) {
            // Simulate an operation on each node (e.g., processing the path)
            // cout << "Processing: " << current->data << endl;  // Uncomment to print
            current = current->next;
        }
    }
};

// Collect all paths in the directory into a linked list
LinkedList collect_paths_into_linked_list(const string& root_directory) {
    LinkedList linked_list;
    for (const auto& entry : recursive_directory_iterator(root_directory)) {
        linked_list.insert(entry.path().string());  // Insert each path into the linked list
    }
    return linked_list;
}

// Perform operations on the linked list and measure complexities
void perform_operations_on_linked_list(LinkedList& linked_list) {
    // Measure space complexity (approximation)
    size_t space_used = sizeof(linked_list) + linked_list.size * sizeof(Node);

    // Time the traversal
    auto start_time = high_resolution_clock::now();
    linked_list.traverse_and_apply_operations();
    auto end_time = high_resolution_clock::now();
    
    duration<double> time_taken = end_time - start_time;

    // Output the data in the required format
    cout << "Directory Traversal, O(n), O(n), "
         << time_taken.count() << " seconds, " << space_used << " bytes" << endl;
}

// Main function
int main() {
    // Define the root directory (adjust this to your actual directory path)
    string root_directory = "/Volumes/CD/pCLE";  // Adjust the path as needed

    // Step 1: Collect all paths into the linked list
    LinkedList linked_list = collect_paths_into_linked_list(root_directory);

    // Step 2: Perform operations on the linked list and measure complexities
    perform_operations_on_linked_list(linked_list);

    return 0;
}
