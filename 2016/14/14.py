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

def getFirstTriple(s):
  for i in range(len(s)-2):
    if s[i] == s[i+1] and s[i] == s[i+2]:
      return s[i]
  return ''

salt = 'cuanljph'
# salt = 'abc'

candidates = []
key_idx = []
i = 0
while len(key_idx) < 64:
  hsh = md5.new(salt + str(i)).hexdigest()
  if args.problem == 2:
    for j in range(2016):
      hsh = md5.new(hsh).hexdigest()
  
  letter = getFirstTriple(hsh)
  if letter != '':
    # print i, letter, hsh
    candidates.append((letter,i))
  
  remaining_candidates = []
  for candidate in candidates:
    letter = candidate[0]
    j = candidate[1]
    if i - j <= 1000:
      if 5*letter in hsh and i - j > 0:
        # print 'found', i, letter, hsh, j
        key_idx.append(j)
      else:
        remaining_candidates.append(candidate)
  candidates = remaining_candidates
  i += 1

key_idx.sort()
print key_idx[63]