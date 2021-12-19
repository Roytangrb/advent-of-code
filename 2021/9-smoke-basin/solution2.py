import heapq

hmap = []

with open('input2.txt', 'r') as f:
    for line in f:
        hmap.append([int(c) for c in line.strip()])

m = len(hmap)
n = len(hmap[0])

def check(i, j):
    curr = hmap[i][j]
    if i-1 in range(m) and hmap[i-1][j] <= curr:
        return False
    if i+1 in range(m) and hmap[i+1][j] <= curr:
        return False
    if j-1 in range(n) and hmap[i][j-1] <= curr:
        return False
    if j+1 in range(n) and hmap[i][j+1] <= curr:
        return False
    return True

def dfs(i, j):
    if i < 0 or i == m or j < 0 or j == n:
        return 0
    curr = hmap[i][j]
    if curr == 9 or curr == -1:
        return 0
    hmap[i][j] = -1
    return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j+1) + dfs(i, j-1)


largest = [0, 0, 0]
for i in range(m):
    for j in range(n):
        if hmap[i][j] not in (-1, 9) and check(i, j):
            size = dfs(i, j)
            if size > largest[0]:
                heapq.heappop(largest)
                heapq.heappush(largest, size)
                
print(largest[0] * largest[1] * largest[2])