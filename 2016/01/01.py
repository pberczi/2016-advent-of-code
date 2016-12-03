#!/usr/bin/python

import argparse
import numpy as np

# parse command line args
parser = argparse.ArgumentParser()
parser.add_argument("input", metavar="input_path", type=str, help="path to input file")
args = parser.parse_args()

# read input file
path = open(args.input, 'r').read().strip().split(', ')

v = (0,1)
x = 0
y = 0

visited = set()
visited.add((x,y))

for move in path:
  # get rotation matrix
  if move[0] == 'L':
    v = (-v[1], v[0])
  elif move[0] == 'R':
    v = (v[1], -v[0])
  else:
    raise ValueError

  # move in that direction
  for i in range(int(move[1:])):
    x += v[0]
    y += v[1]
    if (x,y) in visited:
      print 'duplicate:', (x,y), abs(x) + abs(y)
    visited.add((x,y))

print 'final:', (x,y), abs(x) + abs(y)