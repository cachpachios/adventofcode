from utils import *
import sys
import string
from collections import Counter
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE)[0]

answer = None

for i in range(0,len(file)):
    if len(set(file[i:i+14])) == 14:
        answer = i+14
        break

print("Answer:", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)