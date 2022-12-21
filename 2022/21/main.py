from multiprocessing import Pool
from typing import Dict
from utils import *
from enum import Enum
import sys
import string
from tqdm import tqdm
import math
import numpy as np
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, combinations_with_replacement
from dataclasses import dataclass

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)

@dataclass
class Op:
    a: Any | str
    b: Any | str
    f: Callable[[int, int], int]    
    op: str

mnks = {}

for input in file:
    rs = input.split(":")
    name = rs[0]
    yell = rs[1].strip()
    if yell.isnumeric():
        mnks[name] = int(yell)
    else:
        if '+' in yell:
            splt = yell.split("+")
            mnks[name] = Op(splt[0].strip(), splt[1].strip(), lambda a, b: a + b, "+")
        elif '*' in yell:
            splt = yell.split("*")
            mnks[name] = Op(splt[0].strip(), splt[1].strip(), lambda a, b: a * b, "*")
        elif '-' in yell:
            splt = yell.split("-")
            mnks[name] = Op(splt[0].strip(), splt[1].strip(), lambda a, b: a - b, "-")
        elif '/' in yell:
            splt = yell.split("/")
            mnks[name] = Op(splt[0].strip(), splt[1].strip(), lambda a, b: a // b, "/")
        else:
            raise Exception("Unknown op")
        
def dfnk(v):
    if isinstance(v, int):
        return v
    if isinstance(v, str):
        return "x"
    
    a = dfnk(v.a) 
    b = dfnk(v.b)
    if isinstance(a, int) and isinstance(b, int):
        return v.f(a, b)
    return f"({a} {v.op} {b})"

# Part 1:
#print("Part 1", dfnk(mnks["root"]))

mnks["humn"] = "x" # Part 2

for name, v in mnks.items():
    if not isinstance(v, int) and not isinstance(v, str):
        v.a = mnks[v.a]
        v.b = mnks[v.b]

    
a = dfnk(mnks["root"].a)
b = dfnk(mnks["root"].b)


from sympy.parsing.sympy_parser import parse_expr

if isinstance(a, str):
    a = parse_expr(a)
if isinstance(b, str):
    b = parse_expr(b)
print(a)
print(b)

#Easy to solve by hand to:
answer = 3715799488132

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
exit()
