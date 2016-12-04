#!/usr/bin/python

import argparse
from itertools import permutations

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

travel_times = {}
places = set()
for line in data:
  route = line.split()
  src = route[0]
  dst = route[2]
  time = int(route[4])
  places.add(src)
  places.add(dst)
  travel_times[tuple(sorted([src, dst]))] = time

routes = list(permutations(places))
min_time = float('Inf')
max_time = 0
for route in routes:
  time = 0
  for i in range(1,len(route)):
    src_dst = tuple(sorted([route[i-1], route[i]]))
    time += travel_times[src_dst]
  if time < min_time:
    min_time = time
  if time > max_time:
    max_time = time

print min_time, max_time