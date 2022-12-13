from utils import *
import sys
import string
import functools
from tqdm import tqdm
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE)

blocks = parse_blocks(file)
data = [[eval(l) for l in b] for b in blocks]

def comp(a, b):
    if isinstance(a, int) and isinstance(b, int):
            return int(a < b) - int(a > b)
    elif isinstance(a, list):
        if isinstance(b, int):
            return comp(a, [b])
        elif isinstance(b, list):
            for i in range(min(len(a), len(b))):
                v = comp(a[i], b[i])
                if v != 0:
                    return v

            return int(len(a) < len(b)) - int(len(a) > len(b))
    elif isinstance(a, int) and isinstance(b, list):
        return comp([a], b)
    else:
        raise Exception("??? You bugged out...")

answer = 0

flattended = flatten(data)

flattended.append([[2]])
flattended.append([[6]])

srted = sorted(flattended, key=functools.cmp_to_key(lambda a,b: comp(a,b)), reverse=True)

answer = (srted.index([[6]])+1) * (srted.index([[2]]) + 1)
print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)