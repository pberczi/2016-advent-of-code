#!/usr/bin/python

import argparse
import numpy as np

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

def rect(pixels, width, height):
    pixels[:height,:width] = np.ones((height,width))

def rotRow(pixels, row, amnt):
    pixels_copy = np.copy(pixels)
    for i in range(pixels.shape[1]):
        pixels[row,i] = pixels_copy[row,(i-amnt) % pixels.shape[1]]

def rotCol(pixels, col, amnt):
    pixels_copy = np.copy(pixels)
    for i in range(pixels.shape[0]):
        pixels[i,col] = pixels_copy[(i-amnt) % pixels.shape[0],col]

np.set_printoptions(linewidth=300)

pixels = np.zeros((6,50))
# pixels = np.zeros((3,7))

for line in data:
    instr = line.split()
    if instr[0] == 'rect':
        width = int(instr[1].split('x')[0])
        height = int(instr[1].split('x')[1])
        # rect(pixels, width, height)
        pixels[:height,:width] = 1
    elif instr[1] == 'row':
        row = int(instr[2].split('=')[1])
        amnt = int(instr[4])
        # rotRow(pixels, row, amnt)
        pixels[row,:] = np.concatenate((pixels[row,-amnt:], pixels[row,:-amnt]))
    elif instr[1] == 'column':
        col = int(instr[2].split('=')[1])
        amnt = int(instr[4])
        # rotCol(pixels, col, amnt)
        pixels[:,col] = np.concatenate((pixels[-amnt:, col], pixels[:-amnt,col]))

print np.count_nonzero(pixels)

for row in range(pixels.shape[0]):
    s = ''
    for col in range(pixels.shape[1]):
        if pixels[row][col] == 1:
            s += 'x'
        else:
            s += ' '
    print s
