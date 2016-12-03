#!/usr/bin/python

import argparse
import numpy as np

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
for i in range(0,len(triangles[0]), 3):
  if valid_triangle(tuple(triangle)):
    count += 1

print count
