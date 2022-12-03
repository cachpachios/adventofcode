from utils import *
import sys
import string
from collections import Counter
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE, list)

answer = 0

positions = {
    e: i+1 for i,e in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}

badges = []

for i in range(len(file)//3):
    a = set(file[3*i])
    b = set(file[3*i+1])
    c = set(file[3*i+2])

    badges.append(a.intersection(b).intersection(c).pop())

answer = sum(apply(badges, lambda x: positions[x]))

print(badges)



print("Answer:", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)