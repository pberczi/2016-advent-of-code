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

def genMolecules(base, sub, val):
  molecules = []
  i = 0
  while True:
    i = base.find(sub, i)
    if i == -1:
      break
      
    molecules.append(base[0:i] + base[i:].replace(sub,val,1))
    i += len(sub)
  return molecules

molecule = data[-1]
subs = {}
for line in data[:-1]:
  line = line.split()
  if len(line) == 0:
    continue
  if line[0] not in subs:
    subs[line[0]] = []
  subs[line[0]].append(line[2])

print subs
print molecule

distinct_molecules = set()
for sub in subs:
  print 'computing subs for', sub
  for val in subs[sub]:
    molecules = genMolecules(molecule, sub, val)
    for m in molecules:
      distinct_molecules.add(m)
print
print 'distinct molecules', len(distinct_molecules)
print

reverse_subs = {}
for sub in subs:
  for val in subs[sub]:
    if val not in reverse_subs:
      reverse_subs[val] = []
    reverse_subs[val].append(sub)

# print reverse_subs

backwards = True
gen_molecules = set()
queue = []
subs_in_use = {}
if backwards:
  gen_molecules.add(molecule)
  queue = [(molecule,0)]
  subs_in_use = reverse_subs
else:
  gen_molecules.add('e')
  queue = [('e',0)]
  subs_in_use = subs

gens = set()
gens.add(0)
max_len = 0
min_len = len(molecule)
last = 0
while len(queue) > 0:
  base = queue.pop(0)
  gen = base[1] + 1
  if len(gen_molecules) / 100000 > last:
    print 'currently at gen', gen, len(gen_molecules)
    last = len(gen_molecules) / 100000;
  
  for sub in subs_in_use:
    for val in subs_in_use[sub]:
      molecules = genMolecules(base[0],sub,val)
      for m in molecules:
        if (backwards and m == 'e') or (not backwards and m == molecule):
          print 'generated medicine in', gen, 'steps'
          exit()
        if len(m) < len(molecule) and m not in gen_molecules:
          gen_molecules.add(m)
          queue.append((m,gen))
          
          if len(gen_molecules) % 1000 == 0:
            # print '\tsorting queue'
            queue.sort(key = lambda t: len(t[0]), reverse=(not backwards))
