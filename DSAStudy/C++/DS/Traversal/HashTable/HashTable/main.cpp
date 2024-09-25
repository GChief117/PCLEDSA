//
//  main.cpp
//  HashTable
//
//  Created by Gunnar Beck on 9/19/24.
//

#include <iostream>
#include <unordered_map>
#include <filesystem>
#include <chrono>

using namespace std;
using namespace filesystem;
using namespace chrono;

// HashTable class to store paths using unordered_map
class HashTable {
public:
    unordered_map<string, string> table;  // Hash table implemented using unordered_map

    // Insert a new path into the hash table
    void insert(const string& key, const string& data) {
        table[key] = data;  // Use the path as the key and value
    }

    // Traverse the hash table (process all paths)
    void traverse_and_apply_operations() {
        for (const auto& pair : table) {
            // Simulate an operation (you can add specific operations here)
            // cout << "Processing path: " << pair.first << endl;  // Uncomment to print paths
        }
    }
};

// Collect all paths in the directory into a hash table
HashTable collect_paths_into_hashtable(const string& root_directory) {
    HashTable hashtable;
    
    for (const auto& entry : recursive_directory_iterator(root_directory)) {
        // Insert each directory and file path into the hash table
        hashtable.insert(entry.path().string(), entry.path().string());
    }
    
    return hashtable;
}

// Perform operations on the hash table and measure time and space complexity
void perform_operations_on_hashtable(HashTable& hashtable) {
    // Measure space complexity (approximation)
    size_t space_used = sizeof(hashtable) + hashtable.table.size() * (sizeof(string) * 2);  // Approximation

    // Time the traversal
    auto start_time = high_resolution_clock::now();
    hashtable.traverse_and_apply_operations();  // Traverse and apply operations
    auto end_time = high_resolution_clock::now();
    
    duration<double> time_taken = end_time - start_time;

    // Output the results
    cout << "Directory Traversal, O(1) on average, O(n), "
         << time_taken.count() << " seconds, " << space_used << " bytes" << endl;
}

// Main function
int main() {
    // Define the root directory (adjust this to your actual directory path)
    string root_directory = "/Volumes/CD/pCLE";  // Adjust the path as needed

    // Step 1: Collect all paths into the hash table
    HashTable hashtable = collect_paths_into_hashtable(root_directory);

    // Step 2: Perform operations on the hash table and measure complexities
    perform_operations_on_hashtable(hashtable);

    return 0;
}
