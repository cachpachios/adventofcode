from utils import *
import sys
import string
from tqdm import tqdm
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"
file = read(INPUT_FILE)

sensors = [(x, y, abs(x - b_x) + abs(y - b_y)) for x, y, b_x, b_y in [nums(x) for x in file]]

answer = None
for s_x, s_y, dist in sensors:
    for delta in range(dist*1.5):
        for x, y in [
            (s_x - dist + delta - 1, s_y - delta),
            (s_x + dist - delta + 1, s_y - delta),
            (s_x - dist + delta - 1, s_y + delta),
            (s_x + dist - delta + 1, s_y + delta),
        ]:
            if  0 <= x <= 4000000 and 0 <= y <= 4000000 and \
                all((abs(x - sx) + abs(y - sy)) > d for sx, sy, d in sensors):
                freq = x * 4000000 + y
                print("Found at", x, y, freq)
                answer = freq
                print("Answer", answer)

                if answer and "-pr" in sys.argv:
                    input("Submit? (CTRL+C to cancel)")
                    submit_solution(answer)
                exit()
