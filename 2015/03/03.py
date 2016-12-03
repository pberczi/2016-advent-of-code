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

moves = data[0]

movemap = {'^': (1,0), 'v': (-1,0), '>': (0,1), '<': (0,-1)}
def movePos(pos, v):
  return (pos[0] + v[0], pos[1] + v[1])

pos = (0,0)
pos2 = (0,0)
houses = set()
houses.add(pos)
santasTurn = True
for move in moves:
  if santasTurn:
    pos = movePos(pos, movemap[move])
    houses.add(pos)
  else:
    pos2 = movePos(pos2, movemap[move])
    houses.add(pos2)

  if args.problem == 2:
    santasTurn = not santasTurn

print len(houses)