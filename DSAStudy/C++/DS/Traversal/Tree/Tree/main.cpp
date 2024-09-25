//
//  main.cpp
//  Tree
//
//  Created by Gunnar Beck on 9/19/24.
//

#include <iostream>
#include <vector>
#include <deque>
#include <chrono>
#include <filesystem>
#include <iomanip>  // For output formatting

using namespace std;
using namespace filesystem;
using namespace chrono;

// Tree Node structure
class Node {
public:
    string data;  // Path stored in the node
    vector<Node*> children;  // Children of the node

    Node(const string& data) : data(data) {}  // Constructor to initialize data
};

// General Tree class
class Tree {
public:
    Node* root;

    Tree() : root(nullptr) {}

    // Insert a new path into the tree
    Node* insert(const string& data, Node* parent = nullptr) {
        Node* new_node = new Node(data);
        if (parent == nullptr) {
            if (root == nullptr) {
                root = new_node;
            } else {
                root->children.push_back(new_node);
            }
        } else {
            parent->children.push_back(new_node);
        }
        return new_node;
    }

    // Pre-order traversal
    void pre_order_traversal(Node* node) {
        if (node == nullptr) return;
        for (auto child : node->children) {
            pre_order_traversal(child);
        }
    }

    // Post-order traversal
    void post_order_traversal(Node* node) {
        if (node == nullptr) return;
        for (auto child : node->children) {
            post_order_traversal(child);
        }
    }

    // In-order traversal (adapted for general trees)
    void in_order_traversal(Node* node) {
        if (node == nullptr) return;
        int half = node->children.size() / 2;
        for (int i = 0; i < half; ++i) {
            in_order_traversal(node->children[i]);
        }
        for (int i = half; i < node->children.size(); ++i) {
            in_order_traversal(node->children[i]);
        }
    }

    // Breadth-First Search (BFS)
    void breadth_first_search() {
        if (root == nullptr) return;
        deque<Node*> queue;
        queue.push_back(root);
        while (!queue.empty()) {
            Node* node = queue.front();
            queue.pop_front();
            for (auto child : node->children) {
                queue.push_back(child);
            }
        }
    }

    // Depth-First Search (DFS)
    void depth_first_search() {
        if (root == nullptr) return;
        vector<Node*> stack;
        stack.push_back(root);
        while (!stack.empty()) {
            Node* node = stack.back();
            stack.pop_back();
            for (auto it = node->children.rbegin(); it != node->children.rend(); ++it) {
                stack.push_back(*it);
            }
        }
    }
};

// Collect all paths in the directory into the general tree
Tree collect_paths_into_tree(const string& root_directory) {
    Tree tree;
    
    Node* root_node = tree.insert(root_directory);  // Insert the root directory as the root of the tree
    
    for (const auto& entry : recursive_directory_iterator(root_directory)) {
        Node* parent_node = tree.insert(entry.path().string(), root_node);  // Insert paths
    }
    
    return tree;
}

// Function to perform operations and measure time and space complexity
void perform_operations_on_tree(Tree& tree) {
    size_t space_used = sizeof(tree);  // Measure space complexity (approximation)

    // Store operation results for output
    struct Result {
        string operation;
        string time_complexity;
        string space_complexity;
        double time_taken;
        size_t space_used;
    };
    vector<Result> results;

    // Pre-order traversal
    auto start = high_resolution_clock::now();
    tree.pre_order_traversal(tree.root);
    auto end = high_resolution_clock::now();
    double time_taken = duration<double>(end - start).count();
    results.push_back({"Pre-order Traversal", "O(n)", "O(n)", time_taken, space_used});

    // Post-order traversal
    start = high_resolution_clock::now();
    tree.post_order_traversal(tree.root);
    end = high_resolution_clock::now();
    time_taken = duration<double>(end - start).count();
    results.push_back({"Post-order Traversal", "O(n)", "O(n)", time_taken, space_used});

    // In-order traversal
    start = high_resolution_clock::now();
    tree.in_order_traversal(tree.root);
    end = high_resolution_clock::now();
    time_taken = duration<double>(end - start).count();
    results.push_back({"In-order Traversal", "O(n)", "O(n)", time_taken, space_used});

    // BFS traversal
    start = high_resolution_clock::now();
    tree.breadth_first_search();
    end = high_resolution_clock::now();
    time_taken = duration<double>(end - start).count();
    results.push_back({"BFS Traversal", "O(n)", "O(n)", time_taken, space_used});

    // DFS traversal
    start = high_resolution_clock::now();
    tree.depth_first_search();
    end = high_resolution_clock::now();
    time_taken = duration<double>(end - start).count();
    results.push_back({"DFS Traversal", "O(n)", "O(n)", time_taken, space_used});

    // Output the results in the desired format
    cout << left << setw(25) << "Operation"
         << setw(20) << "Time Complexity"
         << setw(20) << "Space Complexity"
         << setw(25) << "Time (in seconds)"
         << setw(15) << "Size (in bytes)" << endl;

    for (const auto& result : results) {
        cout << left << setw(25) << result.operation
             << setw(20) << result.time_complexity
             << setw(20) << result.space_complexity
             << setw(25) << fixed << result.time_taken << " seconds"  // Use fixed format for seconds
             << setw(15) << result.space_used << " bytes" << endl;
    }
}

// Main function
int main() {
    // Define the root directory (adjust this to your actual directory path)
    string root_directory = "/Volumes/CD/pCLE";
    
    // Step 1: Collect all paths into the tree
    Tree tree = collect_paths_into_tree(root_directory);
    
    // Step 2: Perform operations on the tree and measure complexities
    perform_operations_on_tree(tree);

    return 0;
}
