#include <Node.hpp>

#include <iostream>

using namespace std;

Node::Node(const int & _generation, const int & _elevator, const Floors & _floors)
    : generation(_generation), elevator(_elevator), floors(_floors) { }

bool Node::operator==(const Node & other) const {
  return (elevator == other.elevator) && (floors == other.floors);
}

map<string, int> Node::getTypes(const Floor & f, const string & category) const {
  map<string, int> types;
  for (auto && item : f) {
    if (item.first.second == category) {
      types[item.first.first]++;
    }
  }
  return types;
}

bool Node::isValid() const {
  for (auto && f : floors) {
    auto microchips = getTypes(f, "microchip");
    auto generators = getTypes(f, "generator");
    if (generators.size() > 0) {
      for (auto && microchip : microchips) {
        auto it = generators.find(microchip.first);
        if (it == generators.end() || microchip.second > it->second) {
          return false;
        }
      }
    }
  }
  return true;
}

vector<Node> Node::genChildren() const {
  vector<Node> children;
  for (int e = elevator - 1; e <= elevator + 1; e += 2) {
    // If the elevator can't go there, ignore
    if (e < 0 || e > 3) {
      continue;
    }
    
    // Get all pairs of items that could be taken
    unordered_set<vector<Item>, ItemVectorHasher> candidates;
    auto & f = floors[elevator];
    for (auto && item : f) {
      vector<Item> candidate_single;
      candidate_single.push_back(item.first);
      candidates.insert(candidate_single);
      for (auto && item2 : f) {
        if (item.first == item2.first && item.second < 2) {
          continue;
        }
        vector<Item> candidate_pair(2);
        candidate_pair[0] = item.first;
        candidate_pair[1] = item2.first;
        candidates.insert(candidate_pair);
      }
    }
    
    // Check all candidates
    for (auto && candidate : candidates) {
      auto floors_new = floors;
      auto & f_old = floors_new[elevator];
      auto & f_new = floors_new[e];
      for (auto && item : candidate) {
        auto it = f_old.find(item);
        it->second--;
        if (it->second == 0) {
          f_old.erase(it);
        }
        f_new[item]++;
      }
      auto child = Node(generation + 1, e, floors_new);
      if (child.isValid()) {
        children.push_back(child);
      }
    }
  }
  return children;
}

ostream & operator<<(ostream & os, const Node & node) {
  os << "generation " << node.generation << "\n";
  for (int i = (int)node.floors.size() - 1; i >= 0; --i) {
    if (node.elevator == i) {
      os << "X ";
    } else {
      os << "  ";
    }
    os << "[ ";
    for (auto & item : node.floors[i]) {
      os << item.first.first[0] << item.first.second[0] << " ";
    }
    os << "]\n";
  };
  return os;
}