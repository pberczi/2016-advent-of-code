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

def hasTriple(s):
  for i in range(len(s)-2):
    if s[i] == s[i+1] and s[i] == s[i+2]:
      return (True,s[i])
  return (False, '')

salt = 'cuanljph'
# salt = 'abc'

candidates = set()
keys = []
key_idx = []
i = 0
while len(keys) < 64:
  hsh = md5.new(salt + str(i)).hexdigest()
  if args.problem == 2:
    for j in range(2016):
      hsh = md5.new(hsh).hexdigest()
  
  (has_triple, letter) = hasTriple(hsh)
  if has_triple:
    # print i, letter, hsh
    candidates.add((hsh,letter,i))
  
  remaining_candidates = set()
  for candidate in candidates:
    letter = candidate[1]
    j = candidate[2]
    if i - j <= 1000:
      if 5*letter in hsh and i - j > 0:
        # print 'found', i, letter, hsh, j
        keys.append(candidate[0])
        key_idx.append(j)
      else:
        remaining_candidates.add(candidate)
  candidates = remaining_candidates
  
  i += 1

key_idx.sort()
print key_idx[63]