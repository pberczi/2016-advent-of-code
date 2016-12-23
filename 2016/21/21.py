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

pwd = 'abcdefgh'
if args.problem == 2:
  pwd = 'fbgdceah'
  data = data[::-1]
# print pwd

for line in data:
  instr = line.split()
  if instr[0] == 'swap':
    if instr[1] == 'position':
      positions = [int(instr[2]), int(instr[-1])]
      x = min(positions)
      y = max(positions)
      pwd = pwd[:x] + pwd[y] + pwd[x+1:y] + pwd[x] + pwd[y+1:]
    elif instr[1] == 'letter':
      x = instr[2]
      y = instr[-1]
      pwd = pwd.replace(x,'.')
      pwd = pwd.replace(y,x)
      pwd = pwd.replace('.',y)
  elif instr[0] == 'rotate':
    amt = 0
    if instr[1] == 'based':
      amt = pwd.find(instr[-1])
      if args.problem == 2:
        amt -= 1
        amt %= len(pwd)
        if amt % 2 == 0:
          amt /= 2
        else:
          amt += 7
          amt /= 2
      if amt >= 4:
        amt += 1
      amt += 1
      amt = -amt
    else:
      amt = int(instr[2])
      if instr[1] == 'right':
        amt = -amt
    if args.problem == 2:
      amt = -amt
    amt %= len(pwd)
    pwd = pwd[amt:] + pwd[:amt]
  elif instr[0] == 'reverse':
    positions = [int(instr[2]), int(instr[4])]
    x = min(positions)
    y = max(positions)
    pwd = pwd[:x] + pwd[x:y+1][::-1] + pwd[y+1:]
  elif instr[0] == 'move':
    x = int(instr[2])
    y = int(instr[-1])
    if args.problem == 2:
      tmp = x
      x = y
      y = tmp
    letter = pwd[x]
    pwd = pwd[:x] + pwd[x+1:]
    pwd = pwd[:y] + letter + pwd[y:]
  # print pwd, instr

print pwd