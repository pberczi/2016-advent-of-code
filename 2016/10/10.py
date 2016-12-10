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

class Bot(object):
    def __init__(self, bot_id, low, high):
        self.id = bot_id
        self.low = low
        self.high = high
        self.chips = []
    
    def addChip(self, chip):
        self.chips.append(chip)
        self.chips.sort()
    
    def __eq__(self, other):
        return self.id == other.id

bots = {}
for line in data:
    instr = line.split()
    if instr[0] == 'bot':
        bot_id = int(instr[1])
        low = (instr[5], int(instr[6]))
        high = (instr[10], int(instr[11]))
        bots[bot_id] = Bot(bot_id, low, high)

for line in data:
    instr = line.split()
    if instr[0] == 'value':
        chip = int(instr[1])
        bot_id = int(instr[5])
        bots[bot_id].addChip(chip)

outputs = {}
changed = True
while changed:
    changed = False
    for bot_id in bots:
        bot = bots[bot_id]
        if len(bot.chips) > 1:
            if bot.chips[0] == 17 and bot.chips[1] == 61:
                print 'bot that compares 17 and 61:', bot.id
            
            if bot.low[0] == 'bot':
                bots[bot.low[1]].addChip(bot.chips[0])
            else:
                if bot.low[1] not in outputs:
                    outputs[bot.low[1]] = []
                outputs[bot.low[1]].append(bot.chips[0])

            if bot.high[0] == 'bot':
                bots[bot.high[1]].addChip(bot.chips[1])
            else:
                if bot.high[1] not in outputs:
                    outputs[bot.high[1]] = []
                outputs[bot.high[1]].append(bot.chips[1])
            
            bot.chips = []
            changed = True

print 'multiple of chip in outputs 0, 1, and 2:', outputs[0][0]*outputs[1][0]*outputs[2][0]