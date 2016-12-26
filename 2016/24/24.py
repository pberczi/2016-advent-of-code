#!/usr/bin/python

import argparse
import numpy as np

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

# find all the targets
target_positions = []
for row in range(len(data)):
  for col in range(len(data[row])):
    if data[row][col].isdigit():
      target_positions.append((data[row][col], (row,col)))
target_positions.sort()
targets = [target_position[0] for target_position in target_positions]
# print targets

# find the shortest distances between targets
distances = {}
for (target, start_pos) in target_positions[:-1]:
  # print target
  queue = [[start_pos]]
  visited = set()
  visited.add(start_pos)
  while (target not in distances or len(distances[target]) < len(targets) - 1):
    path = queue.pop(0)
    (row,col) = path[-1]
    candidates = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
    for (row,col) in candidates:
      if row < 0 or col < 0 or row >= len(data) or col >= len(data[0]):
        continue
      if (row,col) in visited:
        continue
      if data[row][col] == '#':
        continue
      visited.add((row,col))
      queue.append(path + [(row,col)])
      if data[row][col] in targets and data[row][col] > target:
        if target not in distances:
          distances[target] = {}
        if data[row][col] not in distances:
          distances[data[row][col]] = {}
        distances[target][data[row][col]] = len(queue[-1]) - 1
        distances[data[row][col]][target] = len(queue[-1]) - 1
# for src in distances:
#   print src,distances[src]

# solve the travelling salesman problem starting at target 0
queue = [['0']]
min_steps = float('inf')
while len(queue) > 0:
  path = queue.pop(0)
  for neighbour in distances[path[-1]]:
    if neighbour in path:
      continue
    queue.append(path + [neighbour])
    steps = 0
    for i in range(len(queue[-1]) - 1):
      steps += distances[queue[-1][i]][queue[-1][i+1]]
    if args.problem == 2:
      steps += distances[queue[-1][-1]]['0']
    if len(queue[-1]) == len(targets) and steps < min_steps:
      min_steps = steps

print min_steps
