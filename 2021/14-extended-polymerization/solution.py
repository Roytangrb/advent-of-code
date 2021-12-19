from collections import Counter

rules = {}

with open('input2.txt', 'r') as f:
    template = next(f).strip()
    next(f)
    try:
        while line := next(f).strip():
            c, nc = line.split(" -> ")
            rules[c] = nc
    except StopIteration:
        pass
    
steps = 10


def counttmp(template):
    maxc = 0
    minc = float('inf')
    count = Counter(template)
    for k, v in count.items():
        maxc = max(maxc, v)
        minc = min(minc, v)
    return maxc - minc

for step in range(steps):
    i = 0
    while i < len(template) - 1:
        comp = template[i:i+2]
        if comp in rules:
            insert = rules[comp]
            template = template[:i+1] + insert + template[i+1:]
            i += 1
        i += 1

print(counttmp(template))
