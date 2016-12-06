#!/usr/bin/python

import argparse
import json

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

account = json.loads(data[0])

def processList(l):
  total = 0
  for item in l:
    if type(item) == int or type(item) == float:
      total += item
    elif type(item) == dict:
      total += processDict(item)
    elif type(item) == list:
      total += processList(item)
  return total

def processDict(d):
  total = 0
  for (key, val) in d.iteritems():
    if args.problem == 2 and (key == 'red' or val == 'red'):
      return 0
    if type(key) == int or type(key) == float:
      total += key
    elif type(key) == dict:
      total += processDict(key)
    elif type(key) == list:
      total += processList(key)
    
    if type(val) == int or type(val) == float:
      total += val
    elif type(val) == dict:
      total += processDict(val)
    elif type(val) == list:
      total += processList(val)
  return total

total = processDict(account)
print total