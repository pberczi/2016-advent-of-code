#!/usr/bin/python

import argparse

# parse command line args
parser = argparse.ArgumentParser()
parser.add_argument("problem", metavar="problem", type=int, help="part of the question to solve")
parser.add_argument("input", metavar="input_path", type=str, help="path to input file")
args = parser.parse_args()

# read input file
triangles = open(args.input, 'r').readlines()
triangles = [[int(x) for x in triangle.strip().split()] for triangle in triangles]

def valid_triangle((a,b,c)):
  return ((a + b) > c) and ((a + c) > b) and ((b + c) > a)

count = 0
if args.problem == 1:
  for triangle in triangles:
    if valid_triangle(tuple(triangle)):
      count += 1
elif args.problem == 2:
  for col in range(len(triangles[0])):
    for row in range(0, len(triangles), 3):
      a = triangles[row][col]
      b = triangles[row + 1][col]
      c = triangles[row + 2][col]
      if valid_triangle((a,b,c)):
        count += 1
else:
  raise ValueError("{0} is not a valid problem number.".format(args.problem)) 

print count
