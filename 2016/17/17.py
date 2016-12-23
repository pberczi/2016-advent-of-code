#!/usr/bin/python

import argparse
from collections import OrderedDict
import md5

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
  
def doorStates(passpath):
  hsh = md5.new(passpath).hexdigest()
  states = []
  for i in range(4):
    if hsh[i] in 'bcdef':
      states.append(1)
    else:
      states.append(0)
  return states

passcode = data[0]
# passcode = 'hijkl'

paths = OrderedDict()
paths[""] = (0,0)
done = False
while len(paths) > 0:
  (path, (row,col)) = paths.popitem(last=False)
  if (row,col) == (3,3):
    continue
  door_states = doorStates(passcode + path)
  possible_moves = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
  possible_move_names = ['U','D','L','R']
  for i in range(len(possible_moves)):
    new_row = possible_moves[i][0]
    new_col = possible_moves[i][1]
    door = door_states[i]
    if not (0 <= new_row < 4 and 0 <= new_col < 4 and door == 1):
      continue
    
    new_path = path + possible_move_names[i]
    # print new_path
    paths[new_path] = (new_row,new_col)
    if (new_row,new_col) == (3,3):
      print new_path, len(new_path)
      # done = True