from functools import cache

file = 'input2.txt'

fishes = []
with open(file, 'r') as f:
    fishes = [
        int(d) for d in next(f).split(',')
    ]

DAYS = 256

@cache
def solve(timer, days):
    if days > DAYS:
        return 0
    if timer == 0:
        return 1 + solve(6, days+1) + solve(8, days+1)
    return solve(timer-1, days+1)
    
    
ans = len(fishes)
for fish in fishes:
    ans += solve(fish, 1)
    
print(ans)