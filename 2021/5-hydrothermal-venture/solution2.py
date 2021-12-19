m = 0
n = 0

vers = []
hors = []
diags = []

for line in open('input2.txt', 'r'):
    pos1, pos2 = line.strip().split(" -> ")
    x1, y1 = [int(d) for d in pos1.split(',')]
    x2, y2 = [int(d) for d in pos2.split(',')]
    n = max(m, x1, x2)
    m = max(n, y1, y2)
    
    start = (x1, y1)
    end = (x2, y2)
    if x1 == x2:
        vers.append([start, end])
    elif y1 == y2:
        hors.append([start, end])
    elif abs(y1 - y2) == abs(x1 - x2):
        diags.append([start, end])

m += 1
n += 1

beach = [[0] * n for _ in range(m)]

for line in vers:
    start, end = line
    x, y1 = start
    _, y2 = end
    for i in range(min(y1, y2), max(y1, y2)+1):
        beach[i][x] += 1


for line in hors:
    start, end = line
    x1, y = start
    x2, _ = end
    for i in range(min(x1, x2), max(x1, x2)+1):
        beach[y][i] += 1
    
for line in diags:
    start, end = line
    x1, y1 = start
    x2, y2 = end
    ll = abs(x1 - x2) + 1
    dx = 1 if x1 < x2 else -1
    dy = 1 if y1 < y2 else -1
    for i in range(ll):
        beach[y1 + i * dy][x1 + i * dx] += 1

ans = 0
for row in beach:
    for count in row:
        if count >= 2:
            ans += 1

print(ans)