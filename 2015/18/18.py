#!/usr/bin/python

import argparse
import numpy as np

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

def numNeighboursOn(lights, row, col):
  n = 0
  for w_row in range(row - 1, row + 2):
    if w_row < 0 or w_row >= lights.shape[0]:
      continue
    for w_col in range(col - 1, col + 2):
      if w_col < 0 or w_col >= lights.shape[1]:
        continue
      if (w_row != row or w_col != col) and lights[w_row,w_col] == 1:
        n += 1
  return n

lights = np.zeros((100,100), dtype = np.int)
for row in range(len(data)):
  for col in range(len(data[row])):
    if data[row][col] == '#':
      lights[row,col] = 1

if args.problem == 2:
  lights[0,0] = lights[0,99] = lights[99,0] = lights[99,99] = 1

n_iter = 0
max_iter = 100
while n_iter < max_iter:
  cur_lights = np.copy(lights)
  for row in range(lights.shape[0]):
    for col in range(lights.shape[1]):
      n_neighbours_on = numNeighboursOn(cur_lights,row,col)
      if cur_lights[row,col] == 1:
        if n_neighbours_on != 2 and n_neighbours_on != 3:
          lights[row,col] = 0
      else:
        if n_neighbours_on == 3:
          lights[row,col] = 1
  
  if args.problem == 2:
    lights[0,0] = lights[0,99] = lights[99,0] = lights[99,99] = 1

  n_iter += 1

print np.count_nonzero(lights)