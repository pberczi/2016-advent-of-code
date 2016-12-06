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

dicts = [{}, {}, {}, {}, {}, {}, {}, {}]
msg1 = ''
msg2 = ''
for line in data:
  for i in range(len(line)):
    char = line[i]
    if char not in dicts[i]:
      dicts[i][char] = 0
    dicts[i][char] += 1

for d in dicts:
  l = []
  for k in d:
    l.append((d[k], k))
  l.sort(reverse=True)
  msg1 = msg1 + l[0][1]
  msg2 = msg2 + l[-1][1]

print msg1
print msg2