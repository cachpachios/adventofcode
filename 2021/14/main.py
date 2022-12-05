from utils import *
import sys
import string
from tqdm import tqdm
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE)

blocks = parse_blocks(file)

s = blocks[0][0]
rules = parse_split(blocks[1], " -> ")

print(len(rules), rules)


count = Counter(s)
pairs = {}

for i in range(len(s)-1):
    pairs[s[i:i+2]] = 1 + pairs.get(s[i:i+2], 0)

print(pairs)


for i in range(40):
    new_pairs = {}
    for (src, dest) in rules:
        if src in pairs:
            count[dest] += pairs[src]
            new_pairs[src[0] + dest] = pairs[src] + new_pairs.get(src[0] + dest, 0)
            new_pairs[dest + src[1]] = pairs[src] + new_pairs.get(dest + src[1], 0)
    pairs = new_pairs

common = count.most_common()
answer = common[0][1] - common[-1][1]

print("Answer:", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)