#!/usr/bin/python

import argparse
import json

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

account = json.loads(data[0])

# def processDict(d):
#   for key in d:
#     if 

total = 0
for key in account:
  print key
  print key.isnumeric()