import os
import string
import sys
from collections import Counter, defaultdict

from utils import *

DAY = 1
PART = 2

if "-pr" in sys.argv:
    if not os.path.exists("input.txt"):
        download_input(DAY)
    INPUT_FILE = "input.txt"
else:
    INPUT_FILE = "test.txt"

answer = None

blocks = read_blocks(INPUT_FILE)


cals = []

for block in blocks:
    ints = [int(x) for x in block]
    cals.append(sum(ints))

answer = sum(sorted(cals)[-3:])

print("Answer:", answer)

if answer and "-pr" in sys.argv:
    submit_answer(DAY, PART, answer)
