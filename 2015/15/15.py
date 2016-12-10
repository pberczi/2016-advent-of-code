#!/usr/bin/python

import argparse

# parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--problem', metavar='n', type=int, default=1, help='part of the question to solve')
parser.add_argument('input', metavar='input_path', type=str, nargs='?', default='input.txt', help='path to input file')
args = parser.parse_args()

data = []
with open(args.input, 'r') as f:
  data = f.read().splitlines()

ingredients = []

for line in data:
  line = line.replace(',', ' ')
  
  item = line.split()
  ingredient = {}
  ingredient['name'] = item[0][:-1]
  ingredient['capacity'] = int(item[2])
  ingredient['durability'] = int(item[4])
  ingredient['flavor'] = int(item[6])
  ingredient['texture'] = int(item[8])
  ingredient['calories'] = int(item[10])

  ingredients.append(ingredient)

amounts = [0 for i in ingredients]
teaspoons = 100

max_cost = 0
for i in range(teaspoons):
    for j in range(teaspoons - i):
        for k in range(teaspoons - (i + j)):
            l = teaspoons - (i + j + k)
            capacity = ingredients[0]['capacity'] * i
            capacity += ingredients[1]['capacity'] * j
            capacity += ingredients[2]['capacity'] * k
            capacity += ingredients[3]['capacity'] * l
            capacity = max(capacity, 0)
            
            durability = ingredients[0]['durability'] * i
            durability += ingredients[1]['durability'] * j
            durability += ingredients[2]['durability'] * k
            durability += ingredients[3]['durability'] * l
            durability = max(durability, 0)
            
            flavor = ingredients[0]['flavor'] * i
            flavor += ingredients[1]['flavor'] * j
            flavor += ingredients[2]['flavor'] * k
            flavor += ingredients[3]['flavor'] * l
            flavor = max(flavor, 0)
            
            texture = ingredients[0]['texture'] * i
            texture += ingredients[1]['texture'] * j
            texture += ingredients[2]['texture'] * k
            texture += ingredients[3]['texture'] * l
            texture = max(texture, 0)
            
            calories = ingredients[0]['calories'] * i
            calories += ingredients[1]['calories'] * j
            calories += ingredients[2]['calories'] * k
            calories += ingredients[3]['calories'] * l
            
            cost = capacity * durability * flavor * texture
            max_cost = max(cost, max_cost) if calories == 500 else max_cost

print max_cost