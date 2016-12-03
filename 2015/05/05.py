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

def nVowels(word):
  n_vowels = 0
  for char in word:
    if char in 'aeiou':
      n_vowels += 1
  return n_vowels

def hasDoubleLetter(word):
  for i in range(1,len(word)):
    if word[i] == word[i - 1]:
      return True
  return False

bad_strings = ['ab', 'cd', 'pq', 'xy']
def hasBadString(word, bad_strings):
  for bad_string in bad_strings:
    if bad_string in word:
      return True
  return False

def hasRepeatingPair(word):
  for i in range(1,len(word)):
    if word[i-1:i+1] in word[i+1:]:
      return True
  return False

def hasPairWithLetterBetween(word):
  for i in range(2,len(word)):
    if word[i] == word[i-2]:
      return True
  return False

n_nice = 0
for line in data:
  if args.problem == 1:
    if nVowels(line) >= 3 and hasDoubleLetter(line) and not hasBadString(line, bad_strings):
      n_nice += 1
  elif args.problem == 2:
    if hasRepeatingPair(line) and hasPairWithLetterBetween(line):
      n_nice += 1
  else:
    raise ValueError

print n_nice