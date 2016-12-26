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

i = 0
found = False
while not found:
  i += 1
  a = 2538 + i
  expected_out = 0
  found = True
  while a > 0:
    b = a % 2
    a = a // 2
    if b != expected_out:
      found = False
      break
    expected_out = 0 if expected_out == 1 else 1

print i
