#!/usr/bin/python

import argparse
import numpy as np

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

def getMarker(line):
    for i in range(len(line)):
        if line[i] == '(' and ')' in line[i+1:]:
            marker_s = line[i+1:].split(')')[0]
            marker = (int(marker_s.split('x')[0]), int(marker_s.split('x')[1]))
            return marker, line[i+1:].split(')')[1]
    return (0,0), line

compressed = data[0]

multiplier = np.ones((1,len(compressed)), dtype=np.int)
i = 0
while i < len(compressed):    
    if compressed[i] == '(':
        (nchars, nrep), rest = getMarker(compressed[i:])
        
        marker_len = len(str(nchars) + 'x' + str(nrep))
        multiplier[0, i:i + marker_len + 2] = 0
        if args.problem == 1:
            multiplier[0, i + marker_len + 2:i + marker_len + 2 + nchars] = nrep
            i += marker_len + 1 + nchars
        elif args.problem == 2:
            multiplier[0, (i + marker_len + 2):(i + marker_len + 2 + nchars)] *= nrep
            i += marker_len + 1
    
    i += 1

print multiplier.sum()