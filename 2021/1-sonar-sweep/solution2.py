depths = []
for line in open('input2.txt', 'r'):
    depth = int(line)
    depths.append(depth)

ans = 0    
prev = sum(depths[:3])

n = len(depths)
l = 1
r = 3
while r < n:
    ret = sum(depths[l:r+1])
    if ret > prev:
        ans += 1
    prev = ret
    l += 1
    r += 1

print(ans)