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

tiles = [data[0]]
# tiles = ['..^^.']
# tiles = ['.^^.^.^^^^']
n_rows = 40
if args.problem == 2:
  n_rows = 400000
for i in range(n_rows - 1):
  prev_tiles = '.' + tiles[i] + '.'
  new_tiles = ''
  for j in range(len(tiles[i])):
    tile_deps = prev_tiles[j:j+3]
    if tile_deps == '^^.' or tile_deps == '.^^' or tile_deps == '^..' or tile_deps == '..^':
      new_tiles += '^'
    else:
      new_tiles += '.'
  tiles.append(new_tiles)

n_safe = 0
for row in tiles:
  n_safe += row.count('.')

print n_safe