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

ins = []
outs = []
for line in data:
  ins.append(int(line.split('-')[0]))
  outs.append(int(line.split('-')[1]))

ins.sort()
outs.sort()

i = 0
counter = 0;
dcounter = 0;
in_idx = 0;
out_idx = 0;
include_start = 0
first_include = -1
n_include = 0
while i <= 4294967295:
  if in_idx >= len(ins):
    break

  if ins[in_idx] <= outs[out_idx] + 1:
    i = ins[in_idx]
    counter += 1
    dcounter = 1
    in_idx += 1
  else:
    i = outs[out_idx] + 1
    counter -= 1
    dcounter = 0
    out_idx += 1

  if counter == 0:
    include_start = i
    if first_include == -1:
      first_include = i
      print 'found', i

  if counter == 1 and dcounter == 1:
    # print include_start, i
    n_include += i - include_start

n_include += 4294967295 - outs[-1]
print 'n_include', n_include
