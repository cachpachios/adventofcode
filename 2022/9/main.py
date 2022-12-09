from utils import *
import sys
import string
from tqdm import tqdm
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE)

moves = [(l[0], int(l[2:])) for l in file]

rope = [0+0j for _ in range(10)]

step_dict = {
    "U": 1j,
    "D": -1j,
    "R": 1,
    "L": -1
}

tail_positions = {0+0j}

def pull(a, b):
    delta = 0
    if abs(a - b) >= 2:
        delta = sign(a.real - b.real) + sign(a.imag - b.imag) * 1j
    return b + delta

for line in file:
    s = line.split()
    d = s[0]
    m = int(s[1])
    for _ in range(m):
        rope[0] += step_dict[d]
        for i in range(1, 10):
            rope[i] = pull(rope[i - 1], rope[i])
        tail_positions.add(rope[-1])

answer = len(tail_positions)

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)