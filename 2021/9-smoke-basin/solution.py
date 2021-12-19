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

ans1 = 0
for i in range(m):
    for j in range(n):
        if check(i, j):
            ans1 += hmap[i][j] + 1

print(ans1)