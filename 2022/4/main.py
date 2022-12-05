from utils import *
import sys
import string
from collections import Counter
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE)

file = [x.split(',') for x in file]

answer = 0

for l in file:
    a = parse(l[0].split('-'))
    b = parse(l[1].split('-'))
    
    if any([x in range(b[0], b[1]+1) for x in range(a[0], a[1]+1)]) or any([x in range(a[0], a[1]+1) for x in range(b[0], b[1]+1)]):
        answer += 1

print("Answer:", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)