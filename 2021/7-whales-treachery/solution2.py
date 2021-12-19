pos = []

with open('input2.txt', 'r') as f:
    pos = [int(d) for d in next(f).strip().split(',')]


def findcost(target):
    c = 0
    for p in pos:
        gap = abs(target-p)
        c += (1 + gap) * gap / 2
    return c

l = min(pos)
r = max(pos)
cost = float('inf')
cost_i = None
for target in range(l, r+1):
    curr = findcost(target)
    if curr < cost:
        cost = curr
        cost_i = target
    
print(cost, cost_i)