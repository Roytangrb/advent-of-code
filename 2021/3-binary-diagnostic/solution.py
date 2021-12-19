lines = []
for line in open('input.txt', 'r'):
    lines.append(line.strip())

n = len(lines)
m = len(lines[0])

onecount = [0] * m

for i in range(n):
    for j in range(m):
        if lines[i][j] == '1':
            onecount[j] += 1
    
gamma = ''
eps = ''
for i in range(m):
    if onecount[i] >= n - onecount[i]:
        gamma += '1'
        eps += '0'
    else:
        gamma += '0'
        eps += '1'

print(int(gamma, 2) * int(eps, 2))