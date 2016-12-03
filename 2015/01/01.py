#!/usr/bin/python

import argparse

# parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--problem', metavar='n', type=int, default=1, help='part of the question to solve')
parser.add_argument('input', metavar='input_path', type=str, help='path to input file')
args = parser.parse_args()

data = []
with open(args.input, 'r') as f:
  data = f.read().splitlines()

floor = 0
instr = data[0]
entered_basement = False
for i in range(len(instr)):
  char = instr[i]
  if char == '(':
    floor += 1
  elif char == ')':
    floor -= 1
  else:
    raise ValueError

  if not entered_basement and floor == -1:
    print 'to basement:', i + 1
    entered_basement = True

print floor