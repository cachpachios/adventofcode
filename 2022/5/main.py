from utils import *
import sys
import string
from collections import Counter
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE, strip=False)

file = parse_blocks(file)

r_s = file[0][:-1]
moves = [x.split() for x in file[1]]
moves = [(x[1], x[3], x[5]) for x in moves]


n = 9 if "-pr" in sys.argv else 3
stacks = [[] for _ in range(n)]

print("n", n)

for s in r_s:
    line = []
    for i in range(n):
        if s[i*4+1] != " ":
            line.append(s[i*4+1])
        else:
            line.append(None)
    for i, e in enumerate(line):
        if e:
            stacks[i].append(e)

stacks = [list(reversed(x)) for x in stacks]

print(stacks)
print()
for m in moves:
    count = int(m[0])
    from_stack = stacks[int(m[1])-1]
    to_stack = int(m[2])-1
    print(count, from_stack, stacks[to_stack])
    stacks[to_stack].extend(from_stack[-count:])
    stacks[int(m[1])-1] = from_stack[:-count]
    print(stacks, '\n')

answer = ''.join([x[-1] for x in stacks if x])



print("Answer:", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)