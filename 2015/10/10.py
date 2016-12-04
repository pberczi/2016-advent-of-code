#!/usr/bin/python

import argparse

# parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--problem', metavar='n', type=int, default=1,
                    help='part of the question to solve')
parser.add_argument('input', metavar='input_path', type=str, nargs='?', default='input.txt',
                    help='path to input file')
args = parser.parse_args()

def nextSequence(sequence):
  next_sequence = ''
  char = sequence[0]
  n = 1
  for i in range(1, len(sequence)):
    if sequence[i] == char:
      n += 1
    else:
      next_sequence += str(n) + char
      char = sequence[i]
      n = 1
  next_sequence += str(n) + char
  return next_sequence

data = []
with open(args.input, 'r') as f:
  data = f.read().splitlines()

sequences = [data[0]]

n_iter = 50
for i in range(1, n_iter + 1):
  sequences.append(nextSequence(sequences[i-1]))

print len(sequences[40])
print len(sequences[50])