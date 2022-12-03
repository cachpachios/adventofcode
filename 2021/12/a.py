
from collections import defaultdict, Counter


with open("/home/tobii.intra/cn1732/2021/12/input.txt", "r") as f:
    lines = f.readlines()

choices = defaultdict(list)

for l in lines:
    nodes = l.strip().split("-")
    choices[nodes[0]].append(nodes[1])
    choices[nodes[1]].append(nodes[0])

print(choices)

def filter(c, path):
    if c == "start":
        return False    
    if c.islower():
        counter = Counter([p for p in path if p.islower()])
        if counter and counter.most_common()[0][1] > 1:
            return c not in path
    return True

frontier = [("start", [])]
paths = set()
while frontier:
    node,path = frontier.pop()
    if node == 'end':
        final_path = ','.join(path)+",end"
        paths.add(final_path)
    else:
        frontier.extend([(c, path+[node]) for c in choices[node] if filter(c, path)])

print('\n'.join(paths))
print(len(paths))