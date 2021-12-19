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

pairs = Counter()
for i in range(len(template)-1):
    word = template[i] + template[i+1]
    pairs[word] += 1

for step in range(40):
    np = Counter()
    for pair, count in pairs.items():
        np[pair[0]+rules[pair]] += count
        np[rules[pair]+pair[1]] += count
    pairs = np


counts = Counter()
for pair in pairs:
    counts[pair[0]] += pairs[pair]

# last char is O, it never changes
counts[template[-1]] += 1

def diff_min_max(counter):
    maxc = 0
    minc = float('inf')
    for k, v in counter.items():
        maxc = max(maxc, v)
        minc = min(minc, v)
    return maxc - minc

print(counts)
print(diff_min_max(counts))