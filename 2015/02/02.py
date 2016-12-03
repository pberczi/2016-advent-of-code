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

def surfaceArea((l,w,h)):
  return 2 * (l*w + l*h + w*h)

paper_area = 0
ribbon_length = 0
for present in data:
  dims = [int(dim) for dim in present.split('x')]
  area = surfaceArea(tuple(dims))
  extra_area = dims[0] * dims[1] * dims[2] / max(dims)
  paper_area += area + extra_area

  ribbon_length += 2 * (dims[0] + dims[1] + dims[2]) - 2 * max(dims)
  ribbon_length += dims[0] * dims[1] * dims[2]

print 'paper_area', paper_area
print 'ribbon_length', ribbon_length