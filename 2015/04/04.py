#!/usr/bin/python

import argparse
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

key = data[0]

i = 1
hash = ''
found = False
while not found:
  hasher = md5.new(key + str(i))
  hash = hasher.hexdigest()
  if args.problem == 1:
    if hash[:5] == '00000':
      found = True
      break
  elif args.problem == 2:
    if hash[:6] == '000000':
      found = True
      break
  else:
    raise ValueError
  i += 1

print i, hash