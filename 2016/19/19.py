#!/usr/bin/python

import argparse
import numpy as np
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

print 'part 1'
p1_start = time.time()
n_elves = int(data[0])
# n_elves = 5
gifts = range(n_elves)
# print gifts
while len(gifts) > 1:
  if len(gifts) % 2 == 0:
    gifts = gifts[::2]
  else:
    gifts = gifts[2::2]
  # print gifts
print gifts[0] + 1, time.time() - p1_start

print 'part 2'
p2_start = time.time()
lefts = range(1,n_elves + 1)
rights = range(-1,n_elves - 1)
lefts[-1] = 0
rights[0] = n_elves - 1

dead = []
i = 0
dead_idx = n_elves / 2
skip = False
if n_elves % 2 == 1:
  skip = True

while lefts[i] != i:
  # print 'dead', dead_idx + 1
  lefts[rights[dead_idx]] = lefts[dead_idx]
  rights[lefts[dead_idx]] = rights[dead_idx]
  dead.append(dead_idx)
  
  dead_idx = lefts[dead_idx]
  if skip:
    dead_idx = lefts[dead_idx]
    skip = False
  else:
    skip = True
  
  i = lefts[i]

print i + 1, time.time() - p2_start