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

nodes = {}

for line in data[2:]:
  fs = line.split()[0]
  x = int(fs.split('-')[-2][1:])
  y = int(fs.split('-')[-1][1:])
  used = int(line.split()[2][:-1])
  avail = int(line.split()[3][:-1])
  nodes[(x,y)] = {}
  nodes[(x,y)]['used'] = used
  nodes[(x,y)]['avail'] = avail

viable_pairs = []
for id_a in nodes:
  for id_b in nodes:
    if id_a == id_b:
      continue
    if nodes[id_a]['used'] == 0:
      continue
    if nodes[id_b]['avail'] < nodes[id_a]['used']:
      continue
    viable_pairs.append((id_a,id_b))

print len(viable_pairs)
