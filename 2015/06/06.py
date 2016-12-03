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

lights_on = set()
lights_brightness = dict()
for line in data:
  line = line.replace(',', ' ')
  line = line.replace('turn o', 'turno')
  line = line.replace('through ', '')
  instructions = line.split()
  
  min_row = int(instructions[1])
  max_row = int(instructions[3])
  min_col = int(instructions[2])
  max_col = int(instructions[4])
  for row in range(min_row, max_row + 1):
    for col in range(min_col, max_col + 1):
      if instructions[0] == 'turnon':
        lights_on.add((row,col))
        if (row,col) not in lights_brightness:
          lights_brightness[(row,col)] = 0
        lights_brightness[(row,col)] += 1
      elif instructions[0] == 'turnoff':
        if (row,col) in lights_on:
          lights_on.remove((row,col))
        if (row,col) in lights_brightness:
          if lights_brightness[(row,col)] > 0:
            lights_brightness[(row,col)] -= 1
          else:
            del lights_brightness[(row,col)]
      elif instructions[0] == 'toggle':
        if (row,col) in lights_on:
          lights_on.remove((row,col))
        else:
          lights_on.add((row,col))
        if (row,col) not in lights_brightness:
          lights_brightness[(row,col)] = 0
        lights_brightness[(row,col)] += 2

print len(lights_on)
total_brightness = 0
for light in lights_brightness:
  total_brightness += lights_brightness[light]
print total_brightness