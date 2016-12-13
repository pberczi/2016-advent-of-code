#include <Node.hpp>

#include <fstream>
#include <future>
#include <iostream>
#include <queue>
#include <sstream>

using namespace std;

vector<Node> genChildren(const vector<Node> & nodes, const unordered_set<Node, NodeHasher> & prev_nodes, int start, int end) {
  vector<Node> children;
  children.reserve(5*(end-start));
  for (int i = start; i < end; ++i) {
    auto cur_children = nodes[i].genChildren();
    for (auto && child : cur_children) {
      if (prev_nodes.find(child) == prev_nodes.end()) {
        children.push_back(child);
      }
    }
  }
  return children;
}

int main(int argc, char ** argv) {
  Floors floors;
  
  ifstream file("input2.txt");
  string line;
  while (getline(file, line)) {
    Floor f;
    stringstream line_stream(line);
    string type;
    while (line_stream) {
      string category;
      line_stream >> category;
      if (category.back() == ',' || category.back() == '.') {
        category.pop_back();
      }
      if (category == "microchip" || category == "generator") {
        Item microchip;
        microchip.first = type.substr(0,type.size() - 11);
        microchip.second = category;
        f[microchip]++;
      }
      type = category;
    }
    floors.push_back(f);
  }
  
  // for (unsigned int i = 0; i < floors.size(); ++i) {
  //   cout << "floor " << i << endl;
  //   for (auto && item : floors[i]) {
  //     cout << item.first.first << " " << item.first.second << " ";
  //   }
  //   cout << endl << endl;
  // }
  
  Floors target_floors(4);
  for (auto && f : floors) {
    for (auto && item : f) {
      target_floors[3][item.first] += item.second;
    }
  }
  auto target_node = Node(0,3,target_floors);
  
  unordered_set<Node, NodeHasher> all_nodes;
  auto root = Node(0,0,floors);
  all_nodes.insert(root);
  auto new_nodes = all_nodes;
  
  // cout << root << endl;
  
  int gen = 0;
  while (new_nodes.find(target_node) == new_nodes.end()) {
    auto cur_nodes = new_nodes;
    new_nodes.clear();
    vector<Node> node_vector;
    node_vector.assign(cur_nodes.begin(), cur_nodes.end());
    
    queue<future<vector<Node>>> cur_children;
    int start = 0;
    for (int i = 0; i < 8; ++i) {
      int end = (i + 1) * node_vector.size() / 8;
      cur_children.push(async(launch::async, &genChildren, node_vector, all_nodes, start, end));
      start = end;
    }
    
    while (cur_children.size() > 0) {
      cur_children.front().wait();
      auto thread_children = cur_children.front().get();
      for (auto && child : thread_children) {
        new_nodes.insert(child);
        all_nodes.insert(child);
      }
      cur_children.pop();
    }
    
    // for (auto && child : children) {
    //   new_nodes.insert(child);
    // }
    cout << "GENERATION " << ++gen << endl;
    // if (gen == 2) {
    //   break;
    // }
  }
}