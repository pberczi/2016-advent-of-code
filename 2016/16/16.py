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

a = '10111011111001111'
disk_size = 272
if args.problem == 2:
  disk_size = 35651584

# test problem input
# a = '10000'
# disk_size = 20

data = a

while len(data) < disk_size:
  b = data[::-1]
  b = b.replace('0','x')
  b = b.replace('1','0')
  b = b.replace('x','1')
  data = data + '0' + b

data = data[:disk_size]
checksum = data[:]
while (len(checksum) % 2 == 0):
  new_checksum = ''
  for i in range(0, len(checksum) - 1, 2):
    if checksum[i] == checksum[i+1]:
      new_checksum += '1'
    else:
      new_checksum += '0'
  checksum = new_checksum

print checksum