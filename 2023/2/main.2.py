from multiprocessing import Pool
from typing import Dict
from utils import *
from enum import Enum
import sys
import string
from tqdm import tqdm
import math
import numpy as np
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)

games = {}

for line in file:
    line = line.split()
    game_id = int(line[1][:-1])

    num_cubes = int((len(line) - 2)/2)
    game = []
    game_set = {}
    for i in range(num_cubes):
        ncubes = line[i*2+2]
        cube = line[i*2+3]
        last_cube = cube[-1]
        if last_cube in [",",";"]:
            cube = cube[:-1]
        game_set[cube] = game_set.get(cube, 0) + int(ncubes)
        if last_cube == ";":
            game.append(game_set)
            game_set = {}   
    game.append(game_set)
    games[game_id] = game


CONF = {
    "red": 12,
    "green": 13,
    "blue": 14
}

answer = 0

for game_id, game in games.items():
    game_minimum = {}
    for gameset in game:
        for cube, count in gameset.items():
            game_minimum[cube] = max(game_minimum.get(cube, 0), count)
    power = 1
    for ncube in game_minimum.values():
        power *= ncube
    answer += power
print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
