from utils import *
import sys
import string
from tqdm import tqdm
from collections import Counter, defaultdict
from itertools import combinations, permutations, combinations_with_replacement

INPUT_FILE = 'input.txt' if "-pr" in sys.argv else 'test.txt'

file = read(INPUT_FILE)



dirs = {}

path = "/"

cwr = {}

tree = {}


for l in file:
    splts = l.split(" ")
    if splts[1] == "cd":
        print(path)
        if splts[2] == "/":
            path = "/"        
        elif splts[2] == "..":
            print("cd " + path)
            if path == "/":
                continue
            path = "/".join(path.split("/")[:-1])
        else:
            path += ("/" if path != '/' else '')  + splts[2]
    elif splts[0] == "dir":
        continue
    elif splts[0] != '$':
        tree[path + '/' + splts[1]] = splts[0] 
        

print(tree)
sizes = {}
                
for k, v in tree.items():
    
    assert k.startswith('/'), k
    pths = ('.' + k).split("/")
    
    file = pths[-1]
    cwd = '/'.join(pths[:-1])
    
    for i,p in enumerate(pths[:-1]):
        last_dir = '/'.join(pths[:i+1]).replace('.', '')
        sizes[last_dir] = sizes.get(last_dir, 0) + int(v)

print(sizes)

# Part 1
answer = sum([x for x in sizes.values() if x <= 100000])

# Part 2
av = 70000000 - sizes[""]

for p,s in sorted(sizes.items(),key=lambda x: x[1]):
    print(p,s)
    if s + av >= 30000000:
        answer = s
        break


print("Answer:", answer)

if answer and "-pr" in sys.argv:
    input("Submit? (CTRL+C to cancel)")
    submit_solution(answer)