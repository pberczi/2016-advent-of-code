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

salt = int(data[0])
goal = (31,39)

def isFree(x,y):
    if x < 0 or y < 0:
        return False
    num = (x+y)*(x+y) + 3*x + y + salt
    return str(bin(num))[2:].count('1') % 2 == 0

nodes = [(1,1,0)]
all_nodes = [(1,1)]
while len(nodes) > 0:
    node = nodes.pop(0)
    # print node
    if args.problem == 2 and node[2] == 50:
        break
    X = node[0]
    Y = node[1]
    for (x,y) in [(X-1,Y), (X+1,Y), (X,Y-1), (X,Y+1)]:
        if (x,y) == (node[0],node[1]):
            continue
        # print (x,y), isFree(x,y)
        if args.problem == 1 and (x,y) == goal:
            print 'goal reached in', node[2]+1, 'steps'
            exit()
        if isFree(x,y) and (x,y) not in all_nodes:
            nodes.append((x,y,node[2]+1))
            all_nodes.append((x,y))
    # print
print 'visisted', len(all_nodes), 'nodes'