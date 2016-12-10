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

clues = {}
clues['children'] = 3
clues['cats'] = 7
clues['samoyeds'] = 2
clues['pomeranians'] = 3
clues['akitas'] = 0
clues['vizslas'] = 0
clues['goldfish'] = 5
clues['trees'] = 3
clues['cars'] = 2
clues['perfumes'] = 1

sues = []
for line in data:
  sueline = line.replace(',', ' ').replace(':', ' ').split()
  sue = {}
  for i in range(2, len(sueline) - 1, 2):
    sue[sueline[i]] = int(sueline[i+1])
  the_real_sue = True
  for clue in clues:
    if clue in sue:
      if args.problem == 2 and (clue == 'cats' or clue == 'trees'):
        if sue[clue] <= clues[clue]:
         the_real_sue = False
         break
      elif args.problem == 2 and (clue == 'pomeranians' or clue == 'goldfish'):
        if sue[clue] >= clues[clue]:
          the_real_sue = False
          break
      elif sue[clue] != clues[clue]:
        the_real_sue = False
        break
  
  if the_real_sue:
    print sueline[1]