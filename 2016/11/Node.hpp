#pragma once

#include <map>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

typedef pair<string, string> Item;
typedef map<Item, int> Floor;
typedef vector<Floor> Floors;

class Node;
class Node {
 public:
  Node(const int & _generation, const int & _elevator, const Floors & _floors);
  bool operator==(const Node & other) const;
  bool operator<(const Node & other) const;
  map<string, int> getTypes(const Floor & f, const string & category) const;
  bool isValid() const;
  vector<Node> genChildren() const;
  
  int generation;
  int elevator;
  Floors floors;
};

ostream& operator<<(ostream & os, const Node & node);

template <typename SizeT>
inline void hash_combine(SizeT &seed, const SizeT &value) {
  seed ^= value + 0x9e3779b9 + (seed << 6) + (seed >> 2);
}

struct ItemHasher {
  size_t operator()(const Item & item) const {
    size_t seed0 = hash<string>()(item.first);
    size_t seed1 = hash<string>()(item.second);
    hash_combine(seed0,seed1);
    return seed0;
  }
};

struct ItemVectorHasher {
  size_t operator()(const vector<Item> & items) const {
    ItemHasher item_hasher;
    vector<size_t> seeds;
    for (auto && item : items) {
      seeds.push_back(item_hasher(item));
    }
    
    size_t seed0 = 0;
    for (auto && seed : seeds) {
      hash_combine(seed0,seed);
    }
    return seed0;
  }
};

struct FloorHasher {
  size_t operator()(const Floor & f) const {
    ItemHasher item_hasher;
    vector<size_t> seeds;
    for (auto && item : f) {
      seeds.push_back(item_hasher(item.first));
      seeds.push_back(hash<int>()(item.second));
    }
    
    size_t seed0 = 0;
    for (auto && seed : seeds) {
      hash_combine(seed0,seed);
    }
    return seed0;
  }
};

struct FloorsHasher {
  size_t operator()(const Floors & floors) const {
    FloorHasher floor_hasher;
    vector<size_t> seeds;
    for (unsigned int i = 0; i < floors.size(); ++i) {
      seeds.push_back(hash<int>()(i));
      seeds.push_back(floor_hasher(floors[i]));
    }
    
    size_t seed0 = 0;
    for (auto && seed : seeds) {
      hash_combine(seed0,seed);
    }
    return seed0;
  }
};

struct NodeHasher {
  size_t operator()(const Node & node) const {
    FloorsHasher floors_hasher;
    size_t seed0 = hash<int>()(node.elevator);
    size_t seed1 = floors_hasher(node.floors);
    hash_combine(seed0,seed1);
    return seed0;
  }
};