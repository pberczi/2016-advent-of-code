#!/usr/bin/python

import argparse
from copy import deepcopy as dc
import itertools as it
from math import ceil

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

boss = {}
boss['hp'] = int(data[0].split()[-1])
boss['atk'] = int(data[1].split()[-1])
boss['def'] = int(data[2].split()[-1])

store = {'weapons':{}, 'armor':{}, 'rings':{}}
section = ''
for line in data[4:]:
  if len(line) == 0:
    continue
  line = line.replace(' +', '+')
  if line.split()[0][:-1].lower() in store:
    section = line.split()[0][:-1].lower()
  else:
    name = line.split()[-4]
    item = {}
    item['cost'] = int(line.split()[-3])
    item['atk'] = int(line.split()[-2])
    item['def'] = int(line.split()[-1])
    store[section][name] = dc(item)

item = {'cost': 0, 'atk': 0, 'def': 0}
store['armor']['none'] = dc(item)
store['rings']['none1'] = dc(item)
store['rings']['none2'] = dc(item)

weapons = store['weapons']
armor = store['armor']
rings = store['rings']

min_cost = 9999999
max_cost = 0
for loadout in it.product(weapons, armor, it.combinations(rings,2)):
  my_weapon = weapons[loadout[0]]
  my_armor = armor[loadout[1]]
  my_ring0 = rings[loadout[2][0]]
  my_ring1 = rings[loadout[2][1]]
  
  cost = my_weapon['cost'] + my_armor['cost'] + my_ring0['cost'] + my_ring1['cost']
  atk = my_weapon['atk'] + my_armor['atk'] + my_ring0['atk'] + my_ring1['atk']
  defense = my_weapon['def'] + my_armor['def'] + my_ring0['def'] + my_ring1['def']
  
  turns = ceil(float(boss['hp'])/max(1, atk - boss['def']))
  boss_turns = ceil(100.0/max(1, boss['atk'] - defense))
  
  if boss_turns >= turns and cost < min_cost:
    min_cost = cost
    
  if boss_turns < turns and cost > max_cost:
    max_cost = cost

print 'min cost to win:', min_cost
print 'max cost to lose:', max_cost
