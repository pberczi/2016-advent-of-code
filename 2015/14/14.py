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

t_final = int(data[0])

speeds = {}
for line in data[1:]:
  split_line = line.split()
  name = split_line[0]
  speed = int(split_line[3])
  flytime = int(split_line[6])
  resttime = int(split_line[-2])
  speeds[name] = (speed, flytime, resttime)

distances = []
for name in speeds:
  t = 0
  dist = 0
  flying = True
  while t < t_final:
    if flying:
      dt = min(speeds[name][1], t_final - t)
      t += dt
      dist += dt * speeds[name][0]
    else:
      dt = min(speeds[name][2], t_final - t)
      t += dt
    flying = not flying
  distances.append((dist,name))

distances.sort()

print distances[-1]

distances = {}
points = {}
for t in range(1, t_final + 1):
  for name in speeds:
    if name not in distances:
      distances[name] = 0

    modt = (t-1)%(speeds[name][1] + speeds[name][2])+1
    if modt <= speeds[name][1]:
      distances[name] += speeds[name][0]

  max_dist = max([distances[name] for name in speeds])
  for name in distances:
    if name not in points:
      points[name] = 0

    if distances[name] == max_dist:
      points[name] += 1

print points