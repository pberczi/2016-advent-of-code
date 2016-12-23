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

registers = {'a':7, 'b':0, 'c':0, 'd':0}
if args.problem == 2:
  registers['a'] = 12

i = 0
while i < len(data):
  instr = data[i].split()
  print i, instr, registers
  if instr[0] == 'cpy':
    src = instr[1]
    dst = instr[2]
    if not dst.isalpha():
      i += 1
      continue
    if src.isalpha():
      src = registers[src]
    else:
      src = int(src)
    registers[dst] = src
  elif instr[0] == 'inc':
    src = instr[1]
    if not src.isalpha():
      i += 1
      continue
    registers[src] += 1
  elif instr[0] == 'dec':
    src = instr[1]
    if not src.isalpha():
      i += 1
      continue
    registers[src] -= 1
  elif instr[0] == 'jnz':
    src = instr[1]
    dst = instr[2]
    if src.isalpha():
      src = registers[src]
    else:
      src = int(src)
    if dst.isalpha():
      dst = registers[dst]
    else:
      dst = int(dst)
    if src > 0:
      i += dst - 1
  elif instr[0] == 'tgl':
    src = instr[1]
    if src.isalpha():
      src = registers[src]
    else:
      src = int(src)
    if i+src >= len(data):
      i += 1
      continue
    if data[i+src].split()[0] == 'inc':
      data[i+src] = 'dec ' + data[i+src].split()[1]
    elif data[i+src].split()[0] == 'dec':
      data[i+src] = 'inc ' + data[i+src].split()[1]
    elif data[i+src].split()[0] == 'jnz':
      data[i+src] = 'cpy ' + data[i+src].split()[1] + ' ' + data[i+src].split()[2]
    elif data[i+src].split()[0] == 'cpy':
      data[i+src] = 'jnz ' + data[i+src].split()[1] + ' ' + data[i+src].split()[2]
    elif data[i+src].split()[0] == 'tgl':
      data[i+src] = 'inc ' + data[i+src].split()[1]
  i += 1

print registers