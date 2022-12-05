from utils import *
import sys
import string
from collections import Counter
from itertools import combinations, permutations, combinations_with_replacement

import numpy as np

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE)
blocks = parse_blocks(file)

dots = blocks[0]
folds = apply(parse_split(blocks[1]),lambda x: x[2].split("="))

x_max = max(parse(extract_n(where(folds, lambda x: x[0]=='x'), 1)))
y_max = max(parse(extract_n(where(folds, lambda x: x[0]=='y'), 1)))

map = np.zeros((y_max*2+1, x_max*2+1), dtype=np.int32)

print(map.shape)

for dot in dots:
    x,y = apply(dot.split(","), int)
    map[y, x] = 1

answer = None


for fold in folds:
    if fold[0] == 'x':
        x = int(fold[1])
        old_map = map
        map = map[:,:x]
        map += np.flip(old_map[:,(x+1):], 1)
    else:
        y = int(fold[1])
        old_map = map
        map = map[:y,:]
        map += np.flip(old_map[(y+1):,:], 0)
    print(map.shape)

for row in map:
    print("".join(["#" if x else "." for x in row]))

answer = input("Answer: ")

print("Answer:", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)