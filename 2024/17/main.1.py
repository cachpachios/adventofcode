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
from itertools import combinations, permutations, combinations_with_replacement, product
from dataclasses import dataclass

from multiprocessing import Pool

from functools import cache, lru_cache

INPUT_FILE = "input.txt" if "-pr" in sys.argv else "test.txt"

file = read(INPUT_FILE)
answer = 0

rrregs, rprgm = parse_blocks(file)


prog = []
regs = {}

for r in rrregs:
    t, v = r.split(": ")
    regs[t[-1]] = int(v)

rprgm = rprgm[0].split(": ")[-1].split(",")
for r in rprgm:
    prog.append(int(r))


def cmb(v, regs):
    if v in range(0, 4):
        return v
    if v == 4:
        return regs["A"]
    if v == 5:
        return regs["B"]
    if v == 6:
        return regs["C"]
    raise ValueError("Invalid value " + str(v))


output = []


# The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.

# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.

# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.

# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)

# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)

# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)

# The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)


def exe(program, regs, debug=True):
    i = 0  # instruction pointer
    while True:
        if i >= len(program):
            break
        op = program[i]
        if debug:
            input(f"{i}: {op} {regs} {output}")
        if op == 0:
            cop = cmb(program[i + 1], regs)
            if debug:
                print(f"adv {regs['A']}//2**{cop}")
            regs["A"] = regs["A"] // 2**cop
        elif op == 1:
            if debug:
                print("bxl", regs["B"], program[i + 1])
            regs["B"] = regs["B"] ^ program[i + 1]
        elif op == 2:
            if debug:
                print("bst", regs["C"], program[i + 1])
            cop = cmb(program[i + 1], regs)
            regs["B"] = cop % 8
        elif op == 3:
            if debug:
                print("jnz", regs["A"], program[i + 1])
            if regs["A"] != 0:
                i = program[i + 1]
                continue
        elif op == 4:
            if debug:
                print("bxc", regs["B"], regs["C"])
            _ = program[i + 1]
            regs["B"] = regs["B"] ^ regs["C"]
        elif op == 5:
            if debug:
                print("out", program[i + 1])
            output.append(cmb(program[i + 1], regs) % 8)
        elif op == 6:
            if debug:
                print("bdv", regs["A"], program[i + 1])
            cop = cmb(program[i + 1], regs)
            regs["B"] = regs["A"] // 2**cop
        elif op == 7:
            if debug:
                print("cdv", regs["A"], program[i + 1])
            cop = cmb(program[i + 1], regs)
            regs["C"] = regs["A"] // 2**cop

        i += 2


exe(prog, regs, "-d" in sys.argv)
answer = ",".join(str(x) for x in output)
print("Regs", regs)
print("Answer", answer)
if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)
    exit()
