#!/usr/bin/python

import argparse

# parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--problem', metavar='n', type=int, default=1,
                    help='part of the question to solve')
parser.add_argument('input', metavar='input_path', type=str, nargs='?', default='input.txt',
                    help='path to input file')
args = parser.parse_args()

# read in data
data = []
with open(args.input, 'r') as f:
  data = f.read().splitlines()

sum_sector_ids = 0
for line in data:
  # get room name
  code = line.split('-')[:-1]
  letters = ''
  for a in code:
    letters += a
    letters += '-'
  letters = letters[:-1]
  
  # get letter counts
  map = {}
  for char in letters:
    if char not in map:
      map[char] = 0
    map[char] -= 1

  letter_counts = []
  for char in map:
    letter_counts.append((map[char], char))

  # sort them (negative counts are useful here since 5 > 1 but x < y)
  letter_counts.sort()

  # compare checksums
  query_checksum = ''
  for i in range(5):
    query_checksum = query_checksum + letter_counts[i][1]

  checksum = line.split('-')[-1][-6:-1]
  sector_id = int(line.split('-')[-1][:-7])

  if checksum == query_checksum:
    sum_sector_ids += sector_id

  # decrypt name
  new_letters = ''
  for char in letters:
    if char == '-':
      new_letters += ' '
    else:
      n = ((ord(char) - 97 + sector_id) % 26) + 97
      new_letters += chr(n)

  print new_letters, sector_id

print 'sum of sector ids:', sum_sector_ids