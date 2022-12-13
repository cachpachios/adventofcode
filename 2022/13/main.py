from utils import *
import sys
import string
from tqdm import tqdm
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE)


blocks = parse_blocks(file)

monkeys = {}
monkey_round = {}

def decode_op(op, b):
    if op == "+":
        if b != "old":
            return lambda x: x + b
        else:
            return lambda x: x + x
    elif op == "*":
        if b != "old":
            return lambda x: x * b
        else:
            return lambda x: x * x
    raise NotImplementedError(op)


for block in blocks:
    id = nums(block[0])[0]

    monkeys[id] = nums(block[1])
    op = block[2].split()
    op = op[-2], int(op[-1]) if op[-1].isnumeric() else op[-1]

    test = nums(block[3])[0]
    
    if_true = nums(block[4])[0]
    if_false = nums(block[5])[0]
    monkey_round[id] = (decode_op(*op), test, if_true, if_false)


inspecions = {}

print(monkeys)

test_product = product([x[1] for x in monkey_round.values()])

for _ in tqdm(range(10000)):
    for id, (op, test, if_true, if_false) in monkey_round.items():
        to_keep = []
        for i,item in enumerate(monkeys[id]):
            inspecions[id] = inspecions.get(id, 0) + 1
            monkeys[id][i] = op(item)

            if monkeys[id][i] % test == 0:
                if if_true == id:
                    to_keep.append(i)
                else:
                    monkeys[if_true].append(monkeys[id][i] % test_product)
            else:
                if if_false == id:
                    to_keep.append(i)
                else:
                    monkeys[if_false].append(monkeys[id][i] % test_product)
        monkeys[id] = [a for i,a in enumerate(monkeys[id]) if i in to_keep]
print(inspecions)

ic = Counter(inspecions).most_common(2)
print(ic)
answer = ic[0][1] * ic[1][1]

print("Answer", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)