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

discs = []

for line in data:
  n_pos = int(line.split()[3])
  start_pos = int(line.split()[-1][:-1])
  
  discs.append((n_pos,start_pos))

if args.problem == 2:
  discs.append((11,0))

t = 0
done = False
while not done:
  done = True
  for i in range(len(discs)):
    pos = (discs[i][1] + t) % discs[i][0]
    if pos != (-(i+1)) % discs[i][0]:
      done = False
  t += 1

print t - 1