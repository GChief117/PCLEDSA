//
//  main.cpp
//  Graph
//
//  Created by Gunnar Beck on 9/19/24.
//

#include <iostream>
#include <unordered_map>
#include <vector>
#include <deque>
#include <chrono>
#include <iomanip>  // For formatting
#include <filesystem>

using namespace std;
using namespace filesystem;
using namespace chrono;

// Graph class using an adjacency list
class Graph {
public:
    unordered_map<string, vector<string>> adjList;  // Adjacency list

    // Add an edge between a directory and its contents (subdirectories/files)
    void add_edge(const string& node, const string& neighbor) {
        adjList[node].push_back(neighbor);
    }

    // Breadth-First Search (BFS)
    void bfs(const string& start_node) {
        unordered_map<string, bool> visited;
        deque<string> queue;

        queue.push_back(start_node);
        visited[start_node] = true;

        while (!queue.empty()) {
            string node = queue.front();
            queue.pop_front();

            for (const auto& neighbor : adjList[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.push_back(neighbor);
                }
            }
        }
    }

    // Depth-First Search (DFS)
    void dfs(const string& node, unordered_map<string, bool>& visited) {
        visited[node] = true;

        for (const auto& neighbor : adjList[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, visited);
            }
        }
    }

    void dfs(const string& start_node) {
        unordered_map<string, bool> visited;
        dfs(start_node, visited);
    }
};

// Collect all paths in the directory into a graph
Graph collect_paths_into_graph(const string& root_directory) {
    Graph graph;

    for (const auto& entry : recursive_directory_iterator(root_directory)) {
        string dirpath = entry.path().string();
        if (is_directory(entry.path())) {
            for (const auto& sub_entry : directory_iterator(entry.path())) {
                string subpath = sub_entry.path().string();
                graph.add_edge(dirpath, subpath);  // Add edge between directory and its contents
            }
        }
    }

    return graph;
}

// Function to perform operations and measure time and space complexity
void perform_operations_on_graph(Graph& graph, const string& start_node) {
    // Estimate the space complexity
    size_t space_used = sizeof(graph) + graph.adjList.size() * sizeof(pair<string, vector<string>>);
    
    for (const auto& entry : graph.adjList) {
        space_used += entry.first.capacity() + entry.second.capacity() * sizeof(string);
    }

    // Store results for formatted output
    struct Result {
        string operation;
        string time_complexity;
        string space_complexity;
        double time_taken;
        size_t space_used;
    };
    vector<Result> results;

    // BFS traversal
    auto start_time = high_resolution_clock::now();
    graph.bfs(start_node);
    auto end_time = high_resolution_clock::now();
    double time_taken_bfs = duration<double>(end_time - start_time).count();
    results.push_back({"BFS Traversal", "O(V + E)", "O(V + E)", time_taken_bfs, space_used});

    // DFS traversal
    start_time = high_resolution_clock::now();
    graph.dfs(start_node);
    end_time = high_resolution_clock::now();
    double time_taken_dfs = duration<double>(end_time - start_time).count();
    results.push_back({"DFS Traversal", "O(V + E)", "O(V + E)", time_taken_dfs, space_used});

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
    
    // Step 1: Collect all paths into the graph
    Graph graph = collect_paths_into_graph(root_directory);
    
    // Step 2: Perform operations on the graph and measure complexities
    perform_operations_on_graph(graph, root_directory);

    return 0;
}
