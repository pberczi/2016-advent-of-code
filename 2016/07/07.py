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

def hasAbba(s):
  for i in range(len(s) - 3):
    if s[i:i+2] == s[i+2:i+4][::-1] and s[i] != s[i+1]:
      return True
  return False

def getAbas(s):
  abas = []
  for i in range(len(s) - 2):
    if s[i] == s[i+2] and s[i] != s[i+1]:
      abas.append(s[i:i+3])
  return abas

count = 0
for line in data:
  nline = line.replace('[',' ')
  nline = nline.replace(']',' ')
  pieces = nline.split()
  hyper = False
  if line[0] == '[':
    hyper = True
  addit = False
  for piece in pieces:
    if not hyper:
      if hasAbba(piece):
        addit = True
    hyper = not hyper

  hyper = False
  if line[0] == '[':
    hyper = True
  for piece in pieces:
    if hyper:
      if hasAbba(piece):
        addit = False
    hyper = not hyper
  
  if addit:
    count += 1

print count

count = 0
for line in data:
  nline = line.replace('[',' ')
  nline = nline.replace(']',' ')
  pieces = nline.split()
  hyper = False
  if line[0] == '[':
    hyper = True
  addit = False
  abas = []
  for piece in pieces:
    if not hyper:
      abas += getAbas(piece)
    hyper = not hyper
  if len(abas) > 0:
    addit = True

  hyper = False
  if line[0] == '[':
    hyper = True
  addit2 = False
  for piece in pieces:
    if hyper:
      for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        if bab in piece:
          addit2 = True
    hyper = not hyper
  
  if addit and addit2:
    count += 1

print count