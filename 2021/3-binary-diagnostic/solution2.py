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

    
found = False
oxy = list(range(n))
for i in range(m):
    c0 = 0
    c1 = 0
    
    if found: break
    
    for j in oxy:
        if lines[j][i] == '1':
            c1 += 1
        else:
            c0 +=1
    most = '1' if c1 >= c0 else '0'
    bk = [d for d in oxy]
    for j in bk:
        if lines[j][i] != most and j in oxy:
            oxy.remove(j)
            if len(oxy) == 1:
                found = True
                break

found = False
co2 = list(range(n))
for i in range(m):
    c0 = 0
    c1 = 0
    
    if found: break
    
    for j in co2:
        if lines[j][i] == '1':
            c1 += 1
        else:
            c0 += 1
    least = '0' if c0 <= c1 else '1'
    bk = [d for d in co2]
    for j in bk:
        if lines[j][i] != least and j in co2:
            co2.remove(j)
            if len(co2) == 1:
                found = True
                break
    
    
print(lines[oxy[0]], lines[co2[0]])
print(int(lines[oxy[0]], 2) * int(lines[co2[0]], 2))
