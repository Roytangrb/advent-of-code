import sys
import heapq

cav = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        cav.append([int(c) for c in line.strip()])

repeat = 5
n = len(cav)
nn = n * repeat
new_cav = [[0] * nn for _ in range(nn)]
for r in range(n):
    for c in range(n):
        new_cav[r][c] = cav[r][c]

for i in range(1, repeat):
    for r in range(n):
        for c in range(n):
            new_val = new_cav[r][c+(i-1)*n] + 1
            new_cav[r][c+i*n] = new_val if new_val <= 9 else 1
    
for r in range(n, nn):
    for c in range(nn):
        new_val = new_cav[r-n][c] + 1
        new_cav[r][c] = new_val if new_val <= 9 else 1

G = new_cav
n = len(G)


forest = [(0, (0, 0))]
spt = set()

def get_neighbors(r, c):
    return [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

while forest:
    cost, pos = heapq.heappop(forest)
    if pos == (n-1, n-1):
        break
    if pos in spt:
        continue
    spt.add(pos)
    
    for nei in get_neighbors(*pos):
        nx, ny = nei
        if 0 <= nx < n and 0 <= ny < n and nei not in spt:
            heapq.heappush(forest, (cost + G[nx][ny], nei))

print(cost)
            