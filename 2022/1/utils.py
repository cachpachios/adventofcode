from typing import Callable, List

## Parsers

def parse_split(input: str, parser: Callable = int, split_str: str = ','):
    if isinstance(parser, list):
        return [parser[i](x) for i, x in enumerate(input.split(split_str))]
    else:
        return [parser(x) for x in input.split(split_str)]

def parse_line(input: List[str], parser: Callable = parse_split):
    return [parser(x) for x in input]
## IO

def read_lines(path: str):
    with open(path, "r") as f:
        return [x.strip() for x in f.readlines() if x.strip() != ""]


def read_ints(path: str):  # 1 => [1]
    return [int(x) for x in read_lines(path)]


def read_ints_comma(path: str):  # 1,2,3,4 => [[1,2,3,4]]
    return [[int(x) for x in line.split(",")] for line in read_lines(path)]


def read_lines_chars(path: str):  # abcdefg => [[a,b,c,d,e,f,g]]
    return [list(x) for x in read_lines(path)]


def read_lines_comma(path: str):  # abc,abc,abc,abc => [[abc,abc,abc,abc]]
    return [x.split(",") for x in read_lines(path)]


def read_blocks(path: str):  # Parses line seperated blocks
    with open(path, "r") as f:
        lines = [x.strip() for x in f.readlines()]

    blocks = []
    block = []
    for line in lines:
        if line == "":
            blocks.append(block)
            block = []
            continue
        block.append(line)
    if block:
        blocks.append(block)
    return blocks


def read_key_values_seperated(path: str):  #
    with open(path, "r") as f:
        lines = [x.strip() for x in f.readlines()]

    blocks = []
    block = {}
    for line in lines:
        if line == "":
            blocks.append(block)
            block = {}
            continue
        block.update(
            {x[0]: x[1] for x in [splits.split(":") for splits in line.split()]}
        )
    if block:
        blocks.append(block)
    return blocks


def read_key_values(path: str):  # k:v k:v k:v => {k:v, k:v, k:v}
    return read_key_values_seperated(path)[0]


def read_split(path: str, split_word: str, parser: Callable):
    return [[parser(x) for x in l.split(split_word)] for l in read_lines(path)]


## Math


def wrap(x, max, min=0):
    return (x - min) % (max - min) + min


def product(x):
    p = 1
    for i in x:
        p *= i
    return p


## AoC Api Utils

import requests

AOC_COOKIE = "53616c7465645f5f24e7b616e4c899f824dc34bd9c6d64c358f427527146aa37d2a6fcdfe3651d28bbcc7dee9ca32cb3488d543bebdb20ce5d26dc2a6ef10316"
YEAR = "2022"


def download_input(day):
    path = f"input.txt"
    text = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{day}/input",
        headers={"cookie": "session=" + AOC_COOKIE},
    ).text
    if text.endswith("\n"):
        text = text[:-1]
    with open(path, "w") as f:
        f.write(text)
    return path, text

def submit_answer(day: int, level: int, answer):
    print(f"You are about to submit the follwing answer:")
    print(f">>>>>>>>>>>>>>>>> {answer}")
    input("Press enter to continue or Ctrl+C to abort.")
    data = {"level": str(level), "answer": str(answer)}

    response = requests.post(
        f"https://adventofcode.com/{YEAR}/day/{day}/answer",
        headers={"cookie": "session=" + AOC_COOKIE},
        data=data,
    )
    if "You gave an answer too recently" in response.text:
        # You will get this if you submitted a wrong answer less than 60s ago.
        print("VERDICT : TOO MANY REQUESTS")
    elif "not the right answer" in response.text:
        if "too low" in response.text:
            print("VERDICT : WRONG (TOO LOW)")
        elif "too high" in response.text:
            print("VERDICT : WRONG (TOO HIGH)")
        else:
            print("VERDICT : WRONG (UNKNOWN)")
    elif "seem to be solving the right level." in response.text:
        # You will get this if you submit on a level you already solved.
        # Usually happens when you forget to switch from `PART = 1` to `PART = 2`
        print("VERDICT : ALREADY SOLVED")
    else:
        print("VERDICT : OK !")
