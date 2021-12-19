prev = None
count = 0

for line in open('input2.txt', 'r'):
    depth = int(line)
    if not prev:
        prev = depth
        continue
    if depth > prev:
        count += 1
    prev = depth
    
print(count)