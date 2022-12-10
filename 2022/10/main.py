from utils import *
import sys
import string
from tqdm import tqdm
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE)


cycle = 0
x = 1


def cyc(n):
    global cycle, x, ss
    for _ in range(n):
        pix = cycle % 40
        if pix == 0:
            print()
        if pix in [x-1, x, x+1]:
            print("#", end="")
        else:
            print(".", end="")
        cycle += 1

for line in file:
    s = line.split()
    
    if(s[0] == "noop"):
        cyc(1)
    elif(s[0] == "addx"):
        cyc(2)
        x += int(s[1])
        




answer = "ECZUZALR"

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)