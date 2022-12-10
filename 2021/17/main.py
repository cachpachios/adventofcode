from utils import *
import sys
import string
from tqdm import tqdm
from collections import Counter
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE)

target = nums(file[0])

print(target)

def simulate_path(vx, vy):
    x,y = 0,0
    while True:
        x += vx
        y += vy
        #positions.append((x,y))
        if x >= target[0] and x <= target[1] and y >= target[2] and y <= target[3]:
            return True
        elif x > target[1] or y < target[2]:
            return False
        vx = max(0, vx - 1)
        vy -= 1


initials = 0
for vx in tqdm(range(10, 500)):
    for vy in range(-200, 3000):
        if simulate_path(vx, vy):
            initials += 1


answer = initials
print("Answer:", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)