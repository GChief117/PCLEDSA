#include <iostream>
#include <filesystem>
#include <vector>
#include <chrono>
#include <iomanip>

using namespace std;
using namespace filesystem;
using namespace chrono;

int main() {
    // Define the root directory (adjust this to your actual directory path)
    string root_directory = "/Volumes/CD/pCLE";
    
    // Vector to store all paths
    vector<string> all_paths;
    
    // Start timing the directory traversal
    auto start_time = high_resolution_clock::now();
    
    // Traverse the directory and collect all paths
    for (const auto& entry : recursive_directory_iterator(root_directory)) {
        all_paths.push_back(entry.path().string());
    }
    
    // End timing
    auto end_time = high_resolution_clock::now();
    
    // Calculate time taken for traversal in seconds
    duration<double> traversal_time = end_time - start_time;
    
    // Calculate space complexity (size of the vector in bytes)
    size_t space_complexity = all_paths.capacity() * sizeof(string);
    
    // Output only the Directory Traversal information
    cout << "Directory Traversal, O(n), O(n), "
         << fixed << setprecision(6) << traversal_time.count() << " seconds, "
         << space_complexity << " bytes" << endl;

    return 0;
}
