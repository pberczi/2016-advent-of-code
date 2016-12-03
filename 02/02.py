#!/usr/bin/python

import argparse
import numpy as np

# parse command line args
parser = argparse.ArgumentParser()
parser.add_argument("problem", metavar="problem", type=int, help="part of the question to solve")
parser.add_argument("input", metavar="input_path", type=str, help="path to input file")
args = parser.parse_args()

# read input file
instructions = open(args.input, 'r').readlines()
instructions = [ins.strip() for ins in instructions]

keypad = []
row = 0
col = 0
if args.problem == 1:
  keypad.append([1,2,3])
  keypad.append([4,5,6])
  keypad.append([7,8,9])
  row = 1
  col = 1
elif args.problem == 2:
  keypad.append(['x','x',  1,'x','x'])
  keypad.append(['x',  2,  3,  4,'x'])
  keypad.append([ 5,   6,  7,  8,  9])
  keypad.append(['x','A','B','C','x'])
  keypad.append(['x','x','D','x','x'])
  row = 2
  col = 0
else:
  raise ValueError("{0} is not a valid problem number".format(args.problem))

code = []

for ins in instructions:
  for move in ins:
    if move == 'U':
      row = row - 1 if row > 0 and keypad[row - 1][col] != 'x' else row
    elif move == 'D':
      row = row + 1 if row < len(keypad) - 1 and keypad[row + 1][col] != 'x' else row
    elif move == 'L':
      col = col - 1 if col > 0 and keypad[row][col - 1] != 'x' else col
    elif move == 'R':
      col = col + 1 if col < len(keypad[row]) - 1 and keypad[row][col + 1] != 'x' else col
    else:
      raise ValueError("{0} is not a valid direction".format(move))

  code.append(keypad[row][col])

print code