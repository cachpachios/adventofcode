import requests, os,re

from typing import Callable, List, Any
from collections.abc import Iterable
from datetime import datetime


CURRENT_YEAR = int(datetime.now().year)
CURRENT_DAY = int(datetime.now().day)
AOC_COOKIE = os.environ.get("AOC_COOKIE")

if not AOC_COOKIE:
    print("[Warning] AOC_COOKIE not set in environment variables")

def read(path, parser: Callable = lambda x: x, strip = True) -> List[str]:
    with open(path, "r") as f:
        return [parser(line.strip() if strip else line.replace("\n","")) for line in f.readlines()]


def parse_blocks(lines: List[str], seperator: str = "", parser: Callable = lambda x: x) -> List[List[str]]:
    blocks = []
    block = []
    for line in lines:
        if line == seperator:
            blocks.append(block)
            block = []
        else:
            block.append(line)
    if block:
        blocks.append(block)
    return [[parser(x) for x in block] for block in blocks]

def parse(lines: List, parser: Callable = int) -> List[Any]:
    return [parser(line) for line in lines]

def apply(func: Callable, lines: List) -> List[Any]:
    return parse(lines, func)

def parse_split(lines: List[str], seperator: str = " ", parser: Callable = lambda x: x) -> List[List[Any]]:
    return [parse(line.split(seperator), parser) for line in lines]

def parse_comma(lines: List[str], parser: Callable = int) -> List[List[Any]]:
    return parse_split(lines, seperator = ",", parser = parser)


def parse_dict(lines: List[str], seperator: str = ":", value_parser: Callable = lambda x: x, key_parser: Callable = lambda x: x) -> dict:
    return {key_parser(line.split(seperator)[0]): value_parser(line.split(seperator)[1:]) if len(line.split(seperator))>2 else value_parser(line.split(seperator)[1]) for line in lines}

def extract(a, indices):
    return [a[i[0]:i[1]] if isinstance(i, Iterable) and len(i) == 2 else a[i] for i in indices] if isinstance(indices, Iterable) else [x[indices] for x in a]

def csv(line, parser = lambda x:x):
    return parser(line.split(","))

def tuple_func(itr, func):
    return [(x, func(x)) for x in itr]

def order_by(list, weight_func):
    tuples = tuple_func(list, weight_func)
    tuples.sort(key=lambda x: x[1])
    return extract(tuples, 0)

def art_sum(a, d, n):
    return n * (2 * a + (n - 1) * d) / 2

def absl(x):
    if isinstance(x, list):
        return [abs(y) for y in x]
    return abs(x)
def all_sum(x):
    if isinstance(x, list):
        return sum([all_sum(y) for y in x])
    return x

def columnize(matrix):
    return list(zip(*matrix))

def reverse(x):
    return x[::-1]

def nums(a, bound=False):
    if isinstance(a, str):
        return [int(x) for x in re.findall(r"(?=[\ ,])?-?\d+\b" if bound else r"-?\d+", a)]
    if isinstance(a, Iterable):
        return [nums(x, bound) for x in a]
    return a

def numsl(a):
    return [nums(l) for l in a]

def param(func, *args):
    return lambda x: func(*((x,) + args))

def findi(s, pattern, with_end=True, overlap=False):
    return [(m.start(), m.end()) if with_end else m.start() for m in (re.finditer(f"(?={pattern})", s) if overlap else re.finditer(pattern, s))]

def find(s, pattern):
    return re.findall(pattern, s)

## Math

def sign(x):
    return (x > 0) - (x < 0)

def wrap(x, max, min = 0):
    return (x - min) % (max - min) + min

def clamp(x, max, min = 0):
    return max(min(x, max), min)

def product(numbers: List[int]) -> int:
    p = 1
    for n in numbers:
        p *= n
    return p

def window_diff(numbers: List[int]) -> List[int]:
    return [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]

def cum_sum(numbers):
    sums = [numbers[0]]
    for n in numbers[1:]:
        sums.append(sums[-1] + n)
    return sums

## AOC Utils


def get_input(year, day):
    input = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers={"cookie": f"session={AOC_COOKIE}"}).text
    if input.endswith("\n"):
        input = input[:-1]
    return input


def save_submission(year, day, part, solution,verdict):
    submissions = read("submissions.txt")
    submissions.append(f"{year}-{day}-{part}:{solution}={verdict}")
    with open(f"submissions.txt", "w") as f:
        f.write("\n".join(submissions))

def check_prev_submission(year, day, part, solution):
    submissions = read("submissions.txt")
    for submission in submissions:
        if f"{year}-{day}-{part}:{solution}" in submission:
            return submission.split("=")[1].strip()
    return None

def done_part_1(year, day):
    submissions = read("submissions.txt")
    for submission in submissions:
        print(submission)
        if submission.startswith(f"{year}-{day}-1") and submission.endswith("=true"):
            return True
    return False

def remove_prev_submission(year, day, part):
    submissions = read("submissions.txt")
    for submission in submissions:
        if f"{year}-{day}-{part}:" in submission:
            submissions.remove(submission)
    with open(f"submissions.txt", "w") as f:
        f.write("\n".join(submissions))

def submit_solution(solution, year = CURRENT_YEAR, day = CURRENT_DAY, part = None):
    if part is None:
        if done_part_1(year, day):
            part = 2
        else:
            part = 1
        print("Auto part:", part)

    verdict = check_prev_submission(year, day, part, solution)

    if verdict:
        print(f"Already submitted {solution} for {year}-{day}-{part} and got {verdict}")
        if input("Clear it? (y)") == "y":
            remove_prev_submission(year, day, part)
        else:
            return

    resp = requests.post(f"https://adventofcode.com/{year}/day/{day}/answer", headers={"cookie": f"session={AOC_COOKIE}"}, data={"level": part, "answer": solution}).text

    text_data = resp.lower()

    if "too high" in text_data:
        print("SUBMISSION>>> INCORRECT!!! Your answer is too HIGH")
        save_submission(year, day, part, solution, "false_too_high")
    elif "too low" in text_data:
        print("SUBMISSION>>> INCORRECT!!! Your answer is too LOW")
        save_submission(year, day, part, solution, "false_too_low")
    elif "that's not" in text_data:
        print("SUBMISSION>>> INCORRECT!!! Your answer is incorrect")
        save_submission(year, day, part, solution, "false_incorrect")
    elif "you don't seem" in text_data:
        print("SUBMISSION>>> ERROR!!! Incorrect part??")
    elif "you gave an answer" in text_data:
        if "left to wait" in text_data:
            pass#print(SUBtext_data.split("left to wait")[0].split()[-1]
        print("SUBMISSION>>> ERROR!! Timout, you already gave an answer to recently.")
    elif "that's the right answer" in text_data:
        print("SUBMISSION>>> CORRECT!!! WELL DONE!")
        save_submission(year, day, part, solution, "true")
