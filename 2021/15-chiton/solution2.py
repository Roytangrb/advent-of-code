import sys

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

cav = new_cav
n = len(cav)

# cost of entering
dp = [[float('inf')] * n for _ in range(n)]
dp[0][0] = 0

for i in range(1, n):
    # first row
    dp[0][i] = dp[0][i-1] + cav[0][i]
    # first col
    dp[i][0] = dp[i-1][0] + cav[i][0]
    
for r in range(1, n):
    for c in range(1, n):
        dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + cav[r][c]

# seconds pass: adjust dp if enter from right or bottom
for r in range(1, n-1):
    for c in range(1, n-1):
        dp[r][c] = min(
            dp[r-1][c] + cav[r][c],
            dp[r+1][c] + cav[r][c],
            dp[r][c-1] + cav[r][c],
            dp[r][c+1] + cav[r][c],
            dp[r][c],
        )

ans = min(
    dp[n-2][n-2] + cav[n-2][n-1] + cav[n-1][n-1],
    dp[n-2][n-2] + cav[n-1][n-2] + cav[n-1][n-1],
)

print(ans)