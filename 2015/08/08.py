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

code_chars = 0
mem_chars = 0
encode_chars = 0
for line in data:
  code_chars += len(line)
  mem_chars += len(line) - 2
  encode_chars += len(line) + 2
  i = 0
  while i < len(line):
    if line[i] == '\\':
      if line[i+1] == '"' or line[i+1] == '\\':
        mem_chars -= 1
        i += 1
      elif line[i+1] == 'x':
        mem_chars -= 3
        i += 3
    i += 1
  i = 0
  while i < len(line):
    if line[i] == '"' or line[i] == '\\':
      encode_chars += 1
    i += 1

print 'code - mem:', code_chars - mem_chars
print 'encode - code:', encode_chars - code_chars
