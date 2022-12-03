import os
import string
import sys
from collections import Counter, defaultdict

from utils import *

DAY = 2

if "-pr" in sys.argv:
    if not os.path.exists("input.txt"):
        download_input(DAY)
    INPUT_FILE = "input.txt"
else:
    INPUT_FILE = "test.txt"


lines = read_lines(INPUT_FILE)

scores= {
    "A X": 1+3, # Rock rock
    "B X": 1+0, # Paper rock
    "C X": 1+6, # Scissors rock
    
    "A Y": 2+6, # Rock paper
    "B Y": 2+3, # Paper paper
    "C Y": 2+0, # Scissors paper
    
    "A Z": 3+0, # Rock scissors
    "B Z": 3+6,# Paper scissors
    "C Z": 3+3,# Scissors scissors
}


tie = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

lose = {
    "A": "Z",
    "B": "X",
    "C": "Y"
}

win = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

answer = 0
for line in lines:
    line_s = line.split()
    if line_s[1] == "X":
        line_2 = line_s[0] + " " + lose[line_s[0]]
    elif line_s[1] == "Y":
        line_2 = line_s[0] + " " + tie[line_s[0]]
    elif line_s[1] == "Z":
        line_2 = line_s[0] + " " + win[line_s[0]]
    answer += scores[line_2]
    
print("Answer:", answer)

PART = 2

if answer and "-pr" in sys.argv:
    submit_answer(DAY, PART, answer)
