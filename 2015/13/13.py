#!/usr/bin/python

import argparse
import itertools

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

happiness = {}

for line in data:
  info = line.split()
  a = info[0]
  b = info[-1][:-1]
  delta = int(info[3]) if info[2] == 'gain' else -int(info[3])

  if a not in happiness:
    happiness[a] = {}

  happiness[a][b] = delta

if args.problem == 2:
  happiness['LPB'] = {}
  for k in happiness:
    happiness[k]['LPB'] = 0
    happiness['LPB'][k] = 0

arrangements = itertools.permutations(happiness.keys())

best_happiness = 'x'
for arrangement in arrangements:
  total = 0
  for i in range(len(arrangement)):
    a = arrangement[i]
    b = arrangement[(i+1)%len(arrangement)]

    total += happiness[a][b]
    total += happiness[b][a]
  if best_happiness == 'x' or total > best_happiness:
    best_happiness = total

print best_happiness