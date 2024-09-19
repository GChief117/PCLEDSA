//
//  main.cpp
//  BST
//
//  Created by Gunnar Beck on 9/19/24.
//

#include <iostream>
#include <vector>
#include <deque>
#include <chrono>
#include <iomanip>  // For output formatting
#include <filesystem>

using namespace std;
using namespace filesystem;
using namespace chrono;

// Node structure for the BST
class Node {
public:
    string data;
    Node* left;
    Node* right;

    Node(string value) : data(value), left(nullptr), right(nullptr) {}
};

// Binary Search Tree (BST) class
class BST {
public:
    Node* root;

    BST() : root(nullptr) {}

    // Insert a new path into the BST
    void insert(const string& data) {
        if (root == nullptr) {
            root = new Node(data);  // Create the root node
        } else {
            insert_recursive(root, data);
        }
    }

    void insert_recursive(Node* node, const string& data) {
        if (data < node->data) {
            if (node->left == nullptr) {
                node->left = new Node(data);
            } else {
                insert_recursive(node->left, data);
            }
        } else {
            if (node->right == nullptr) {
                node->right = new Node(data);
            } else {
                insert_recursive(node->right, data);
            }
        }
    }

    // In-order traversal
    void in_order_traversal(Node* node) {
        if (node != nullptr) {
            in_order_traversal(node->left);
            in_order_traversal(node->right);
        }
    }

    // Pre-order traversal
    void pre_order_traversal(Node* node) {
        if (node != nullptr) {
            pre_order_traversal(node->left);
            pre_order_traversal(node->right);
        }
    }

    // Post-order traversal
    void post_order_traversal(Node* node) {
        if (node != nullptr) {
            post_order_traversal(node->left);
            post_order_traversal(node->right);
        }
    }

    // Breadth-First Search (BFS)
    void bfs() {
        if (root == nullptr) return;

        deque<Node*> queue;
        queue.push_back(root);
        while (!queue.empty()) {
            Node* node = queue.front();
            queue.pop_front();

            if (node->left != nullptr) {
                queue.push_back(node->left);
            }
            if (node->right != nullptr) {
                queue.push_back(node->right);
            }
        }
    }

    // Depth-First Search (DFS)
    void dfs(Node* node) {
        if (node != nullptr) {
            dfs(node->left);
            dfs(node->right);
        }
    }
};

// Collect all paths in the directory into a BST
BST collect_paths_into_bst(const string& root_directory) {
    BST bst;

    for (const auto& entry : recursive_directory_iterator(root_directory)) {
        string dirpath = entry.path().string();
        bst.insert(dirpath);
    }

    return bst;
}

// Function to perform operations and measure time and space complexity
void perform_operations_on_bst(BST& bst) {
    // Estimate space complexity (approximation)
    size_t space_used = sizeof(bst) + sizeof(Node) * 2;  // Approximation of memory used

    // Store results for formatted output
    struct Result {
        string operation;
        string time_complexity;
        string space_complexity;
        double time_taken;
        size_t space_used;
    };
    vector<Result> results;

    // In-order traversal
    auto start_time = high_resolution_clock::now();
    bst.in_order_traversal(bst.root);
    auto end_time = high_resolution_clock::now();
    double time_taken_in_order = duration<double>(end_time - start_time).count();
    results.push_back({"In-order Traversal", "O(n)", "O(n)", time_taken_in_order, space_used});

    // Pre-order traversal
    start_time = high_resolution_clock::now();
    bst.pre_order_traversal(bst.root);
    end_time = high_resolution_clock::now();
    double time_taken_pre_order = duration<double>(end_time - start_time).count();
    results.push_back({"Pre-order Traversal", "O(n)", "O(n)", time_taken_pre_order, space_used});

    // Post-order traversal
    start_time = high_resolution_clock::now();
    bst.post_order_traversal(bst.root);
    end_time = high_resolution_clock::now();
    double time_taken_post_order = duration<double>(end_time - start_time).count();
    results.push_back({"Post-order Traversal", "O(n)", "O(n)", time_taken_post_order, space_used});

    // Breadth-First Search (BFS)
    start_time = high_resolution_clock::now();
    bst.bfs();
    end_time = high_resolution_clock::now();
    double time_taken_bfs = duration<double>(end_time - start_time).count();
    results.push_back({"BFS Traversal", "O(n)", "O(n)", time_taken_bfs, space_used});

    // Depth-First Search (DFS)
    start_time = high_resolution_clock::now();
    bst.dfs(bst.root);
    end_time = high_resolution_clock::now();
    double time_taken_dfs = duration<double>(end_time - start_time).count();
    results.push_back({"DFS Traversal", "O(n)", "O(n)", time_taken_dfs, space_used});

    // Print the results in the desired format
    cout << left << setw(25) << "Operation"
         << setw(20) << "Time Complexity"
         << setw(20) << "Space Complexity"
         << setw(25) << "Time (in seconds)"
         << setw(15) << "Size (in bytes)" << endl;

    for (const auto& result : results) {
        cout << left << setw(25) << result.operation
             << setw(20) << result.time_complexity
             << setw(20) << result.space_complexity
             << setw(25) << fixed << result.time_taken << " seconds"
             << setw(15) << result.space_used << " bytes" << endl;
    }
}

// Main function
int main() {
    // Define the root directory (adjust this to your actual directory path)
    string root_directory = "/Volumes/CD/pCLE";  // Adjust as needed

    // Step 1: Collect all paths into the BST
    BST bst = collect_paths_into_bst(root_directory);

    // Step 2: Perform operations on the BST and measure complexities
    perform_operations_on_bst(bst);

    return 0;
}
