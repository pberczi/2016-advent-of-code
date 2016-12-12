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

registers = {'a':0, 'b':0, 'c':0, 'd':0}
if args.problem == 2:
  registers['c'] = 1

i = 0
while i < len(data):
  instr = data[i].split()
  if instr[0] == 'cpy':
    src = instr[1]
    dst = instr[2]
    if src.isalpha():
      src = registers[src]
    else:
      src = int(src)
    registers[dst] = src
  elif instr[0] == 'inc':
    src = instr[1]
    registers[src] += 1
  elif instr[0] == 'dec':
    src = instr[1]
    registers[src] -= 1
  elif instr[0] == 'jnz':
    src = instr[1]
    if src.isalpha():
      src = registers[src]
    else:
      src = int(src)
    if src > 0:
      i += int(instr[2]) - 1
  i += 1

print registers