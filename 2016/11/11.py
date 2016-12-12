#!/usr/bin/python

import argparse
import copy
from itertools import combinations
import threading
import time

# parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--problem', metavar='n', type=int, default=1,
                    help='part of the question to solve')
parser.add_argument('input', metavar='input_path', type=str, nargs='?', default='input.txt',
                    help='path to input file')
args = parser.parse_args()

data = []
with open(args.input, 'r') as f:
  data = f.read().splitlines()

class Node(object):
  def __init__(self, generation, elevator, items):
    self.generation = generation
    self.elevator = elevator
    self.items = items
    self.children = []
  
  def __eq__(self, other):
    if self.elevator != other.elevator:
      return False
    for i in range(len(self.items)):
      if sorted(self.items[i]) != sorted(other.items[i]):
        return False
    return True
  
  def __str__(self):
    s = 'generation ' + str(self.generation) + '\n'
    for i in range(len(self.items) - 1, -1, -1):
      s += 'X ' if self.elevator == i else '  '
      s += str(self.items[i]) + '\n'
    return s
  
  def isValid(self):
    for floor in self.items:
      candidate_microchips = [item[0] for item in floor if item[1] == 'microchip']
      candidate_generators = [item[0] for item in floor if item[1] == 'generator']
      if len(candidate_generators) > 0:
        for microchip in candidate_microchips:
          if microchip in candidate_generators:
            candidate_generators.remove(microchip)
          else:
            return False
    return True
  
  def genChildren(self):
    for elevator in [self.elevator - 1, self.elevator + 1]:
      # if the elevator can't go there, ignore this child
      if elevator not in range(4):
        continue
      
      # get all pairs of items that could be taken with us
      items = self.items[self.elevator][:]
      candidates = [[item] for item in items] + [list(combo) for combo in list(combinations(items, 2))]
      
      # check every candidate 
      for candidate in candidates:
        new_items = copy.deepcopy(self.items)
        for item in candidate:
          new_items[self.elevator].remove(item)
          new_items[elevator].append(item)
        child = Node(self.generation + 1, elevator, new_items)
        
        if child not in self.children and child.isValid():
          self.children.append(child)

class ChildrenGenerationThread(threading.Thread):
  def __init__(self, node):
    threading.Thread.__init__(self)
    self.node = node
  
  def run(self):
    self.node.genChildren()

items = []
for line in data:
  words = line.replace(',', ' ').replace('.','').split()
  cur_items = []
  for i in range(len(words)):
    if words[i] == 'generator':
      cur_items.append((words[i-1], 'generator'))
    elif words[i] == 'microchip':
      cur_items.append((words[i-1].split('-')[0], 'microchip'))
  items.append(cur_items)

leaf_items = [[],[],[],[]]
for floor in items:
  for item in floor:
    leaf_items[3].append(item)

max_threads = 8
nodes = [Node(0, 0, items)]
all_nodes = copy.deepcopy(nodes)
leaf = Node(0, 3, leaf_items)
gen = 0
while leaf not in nodes:
  new_nodes = []
  i = 0
  while i < len(nodes):
    if threading.activeCount() < max_threads:
      thread = ChildrenGenerationThread(nodes[i])
      thread.start()
      i += 1
    else:
      time.sleep(0.01)
  
  for node in nodes:
      for child in node.children:
        if child not in all_nodes:
          new_nodes.append(child)
          all_nodes.append(child)
  
  nodes = new_nodes
  gen += 1
  print gen
  if (gen == 10000):
    break
# node 0: initial state
# generate children of node 0
# foreach child, generate its children (can't undo the last move)
# keep track of generation
# when we have a valid output, print the generation
# do this breadth first, stop at first solution