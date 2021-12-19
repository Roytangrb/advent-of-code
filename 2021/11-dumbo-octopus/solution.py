M = []

with open('input2.txt', 'r') as f:
    for line in f:
        M.append([])
        for ch in line.strip():
            M[-1].append(int(ch))

m = len(M)
n = len(M[0])

ans = 0

def dfs(i, j):
    global ans
    if i not in range(m) or j not in range(n):
        return
    if M[i][j] == -1:
        return
    
    M[i][j] += 1
    if M[i][j] > 9:
        M[i][j] = -1
        ans += 1
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i-1, j-1)
        dfs(i-1, j+1)
        dfs(i+1, j-1)
        dfs(i+1, j+1)

step = 100
for _ in range(step):
    for i in range(m):
        for j in range(n):
            dfs(i, j)

    for i in range(m):
        for j in range(n):
            if M[i][j] == -1:
                M[i][j] = 0

for row in M:
    print(row)
print(ans)