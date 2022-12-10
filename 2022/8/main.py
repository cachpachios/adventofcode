from utils import *
import sys
import string
from tqdm import tqdm
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE, list)
map = parse(file, lambda x: [int(a) for a in x])
print(map)


answer = 0

scenic_scores = []

for y in range(len(map[0])):
    for x in range(len(map)):
        if x == 0 or y == 0 or x == len(map)-1 or y == len(map[0])-1:
            continue
        
        this = map[y][x]
        
        above = list(([map[y_][x] for y_ in range(y-1, -1, -1)]))
        below = list(([map[y_][x] for y_ in range(y+1, len(map))]))
        right = ([map[y][x_] for x_ in range(x+1, len(map))])
        left = ([map[y][x_] for x_ in range(x-1, -1, -1)])
        
        print()
        print(x,y, this)
        print("ABOVE BELOW RIGHT LEFT")
        print(list(above), list(below), list(right), list(left))
        
        above = [this > a for a in above] #+ [False]
        below = [this > b for b in below] #+ [False]
        right = [this > r for r in right] #+ [False]
        left = [this > l for l in left] #+ [False]
        
        visbile = any([
            all(above),
            all(left),
            all(below),
            all(right),
        ])
        
        if not visbile:
            continue
        
        print(visbile)
        print(above, below, right, left)
            
        above = [1 for i, a in enumerate(above) if all(above[:i])]
        below = [1 for i, b in enumerate(below) if all(below[:i])]
        right = [1 for i, r in enumerate(right) if all(right[:i])]
        left = [1 for i, l in enumerate(left) if all(left[:i])]
        
        sums = [sum(above), sum(below or [0]), sum(right), sum(left)]
        
        scenic_score = product([n for n in sums if n>0])
        
        print(sums)
        print(above, below, right, left)
        print(scenic_score)
        scenic_scores.append(scenic_score)
print(scenic_scores)
answer = max(scenic_scores)
print("Answer:", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)