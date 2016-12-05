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

def hasStraight(pwd):
  for i in range(2,len(pwd)):
    l1 = pwd[i-2]
    l2 = pwd[i-1]
    l3 = pwd[i]
    if ord(l1) == ord(l2) - 1 and ord(l2) == ord(l3) - 1:
      return True
  return False

def validLetters(pwd, invalid_letters):
  for char in pwd:
    if char in invalid_letters:
      return False
  return True

def hasTwoPairs(pwd):
  pair_1_char = ''
  for i in range(1,len(pwd)):
    if pwd[i-1] == pwd[i]:
      if pair_1_char == '':
        pair_1_char = pwd[i]
      elif pwd[i] != pair_1_char:
        return True
  return False

def incrementString(pwd):
  new_pwd = pwd
  for i in range(len(pwd) - 1, -1, -1):
    if new_pwd[i] == 'z':
      new_pwd = new_pwd[:i] + 'a' + new_pwd[i+1:]
    else:
      new_pwd = new_pwd[:i] + chr(ord(new_pwd[i]) + 1) + new_pwd[i+1:]
      break
  return new_pwd


pwd = data[0]
invalid_letters = 'iol'

valid_pwds = []
while len(valid_pwds) < 2:
  pwd = incrementString(pwd)
  if hasStraight(pwd) and validLetters(pwd, invalid_letters) and hasTwoPairs(pwd):
    valid_pwds.append(pwd)

print valid_pwds