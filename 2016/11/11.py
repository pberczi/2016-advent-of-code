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
  def __init__(self, nodes, prev_nodes):
    threading.Thread.__init__(self)
    self.nodes = nodes
    self.prev_nodes = copy.deepcopy(prev_nodes)
  def run(self):
    for node in self.nodes:
      node.genChildren()
      # for child in node.children:
      #   if child in self.prev_nodes:
      #     node.children.remove(child)

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
  threads = []
  for i in range(max_threads):
    if nodes[i::max_threads] == []:
      continue
    thread = ChildrenGenerationThread(nodes[i::max_threads], all_nodes)
    thread.start()
    threads.append(thread)
  
  for thread in threads:
    thread.join()
  
  for node in nodes:
    all_nodes += node.children
    new_nodes += node.children
  
  nodes = new_nodes
  gen += 1
  print gen
  if gen == 50:
    break
# node 0: initial state
# generate children of node 0
# foreach child, generate its children (can't undo the last move)
# keep track of generation
# when we have a valid output, print the generation
# do this breadth first, stop at first solution