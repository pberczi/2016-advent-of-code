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

def emulate(a, b, gate):
  if gate == 'NOT':
    return ~b
  if gate == 'LSHIFT':
    return a << b
  if gate == 'RSHIFT':
    return a >> b
  if gate == 'AND':
    return a & b
  if gate == 'OR':
    return a | b

wires = {}
if args.problem == 2:
  wires['b'] = 956
queue = []
for line in data:
  instr = line.split()
  if len(instr) == 3:
    instr = [instr[0], 'AND'] + instr
  if len(instr) == 4:
    instr = [instr[1]] + instr
  queue.append(instr)

while len(queue) > 0:
  for instr in queue:
    w1 = instr[0]
    w2 = instr[2]
    gate = instr[1]
    w3 = instr[4]

    if w1.isalpha() and w1 not in wires:
      continue
    if w2.isalpha() and w2 not in wires:
      continue

    w1 = wires[w1] if w1.isalpha() else int(w1)
    w2 = wires[w2] if w2.isalpha() else int(w2)
    
    wires[w3] = emulate(w1,w2,gate)
    queue.remove(instr)

print wires['a']