import sys

cav = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        cav.append([int(c) for c in line.strip()])
        
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
            dp[r-1][c],
            dp[r+1][c],
            dp[r][c-1],
            dp[r][c+1],
        ) + cav[r][c]

ans = min(
    dp[n-2][n-2] + cav[n-2][n-1] + cav[n-1][n-1],
    dp[n-2][n-2] + cav[n-1][n-2] + cav[n-1][n-1],
)

print(ans)