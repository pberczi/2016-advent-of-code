#!/usr/bin/python

import argparse

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

def numCombos(litres, containers):
  end_containers = [[c] for c in containers if c == litres]
  n = len(end_containers)
  possible_containers = [c for c in containers if c < litres]
  for i in range(len(possible_containers)):
    [n_sub, c_sub] = numCombos(litres - possible_containers[i], possible_containers[i+1:])
    n += n_sub
    for c in c_sub:
      end_containers.append([possible_containers[i]] + c)
  return n, end_containers

containers = []
for line in data:
  containers.append(int(line))

containers.sort(reverse=True)
n, combos = numCombos(150, containers)

min_combo = len(containers)
for combo in combos:
  if len(combo) < min_combo:
    min_combo = len(combo)

min_combos = [combo for combo in combos if len(combo) == min_combo]
print n, len(min_combos)
