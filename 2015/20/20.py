#!/usr/bin/python

import argparse
from itertools import combinations
from operator import mul

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

# generate first 1000 primes
primes = [2]
i = 3
while len(primes) < 100000:
  is_prime = True
  for prime in primes:
    if prime > i**0.5:
      break
    if i % prime == 0:
      is_prime = False
      break
  if is_prime:
    primes.append(i)
  i += 2

def primeFactors(x):
  prime_factors = []
  y = x
  found_factor = True
  while found_factor:
    found_factor = False
    for prime in primes:
      if prime > y**0.5:
        if (y in primes):
          prime_factors.append(y)
          y = 1
        break
      if y % prime == 0:
        y = y / prime
        prime_factors.append(prime)
        found_factor = True
        break
  if y > 1:
    raise RuntimeError("not enough primes")
  return prime_factors

def nPresents(x):
  pf = primeFactors(x)
  combos = [combo for combo_list in [list(set(combinations(pf,i+1))) for i in range(len(pf))] for combo in combo_list]
  prods = [reduce(mul,combo) for combo in combos]
  prods += [1]
  n = 0
  for prod in prods:
    if args.problem == 1:
      n += 10 * prod
    elif x < 50*prod:
      n += 11 * prod
  return n

n = int(data[0])

for i in range(10,max(primes)):
  n_presents = nPresents(i)
  if i % 10000 == 0:
    print 'checking house', i, n_presents
  if n_presents >= n:
    print
    print 'FOUND IT', i, n_presents
    break