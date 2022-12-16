from utils import *
import sys
import string
from tqdm import tqdm
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'
file = read(INPUT_FILE)

map = []

starts = []
stop = None

for l in file:
    map.append([])
    for c in l:
        if c == "S" or c == 'a':
            starts.append( ([(len(map)-1, l.index(c))], 1) )
            map[-1].append(0)
        elif c == "E":
            stop = (len(map)-1, l.index(c))
            map[-1].append(len(string.ascii_lowercase))
        else:
            map[-1].append(string.ascii_lowercase.index(c))

for l in map:
    print(' '.join([str(x) for x in l]))

paths = [] # (been, score)

# Populate queue
for (been, score) in starts:
    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x_ = been[-1][0]+x
        y_ = been[-1][1]+y
        if x_ >= 0 and x_ < len(map) and y_ >= 0 and y_ < len(map[0]):
            if (x_, y_) not in been:
                if abs(map[x_][y_] - map[been[-1][0]][been[-1][1]]) <= 1:
                    paths.append((been + [(x_, y_)], score + 1))


final_paths = []

explored = {}

while paths:
    new_paths = []
    
    for (been, score) in paths:
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_ = been[-1][0]+x
            y_ = been[-1][1]+y
            if x_ >= 0 and x_ < len(map) and y_ >= 0 and y_ < len(map[0]):
                if (x_, y_) not in been and (x_, y_) not in explored and score < explored.get((x_, y_), 100000):
                    if map[x_][y_] <= map[been[-1][0]][been[-1][1]] + 1:
                        if (x_, y_) == stop:
                            final_paths.append((been,score))
                        else:
                            new_paths.append((been + [(x_, y_)], score + 1))
                            explored[(x_, y_)] = score
    paths = new_paths

            

print(len(final_paths))


answer = min(final_paths, key=lambda x: x[1])
print(len(answer[0]), answer[1])

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)