#!/usr/bin/python

import argparse
import md5

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

id = data[0]
i = 1
pwd = ''
while len(pwd) < 8:
  hasher = md5.new(id + str(i))
  hash = hasher.hexdigest()
  if hash[0:5] == '00000':
    pwd += hash[5]
  i += 1
print 'part1:', pwd

i = 1
pwd = '        '
while ' ' in pwd:
  hasher = md5.new(id + str(i))
  hash = hasher.hexdigest()
  if hash[0:5] == '00000':
    pos = hash[5]
    if not pos.isalpha() and int(pos) >= 0 and int(pos) < 8 and pwd[int(pos)] == ' ':
      pwd = pwd[:int(pos)] + hash[6] + pwd[int(pos) + 1:]
  i += 1
print 'part2:', pwd