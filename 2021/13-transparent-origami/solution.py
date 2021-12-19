dots = set()
ops = []

with open('input2.txt', 'r') as f:
    try: 
        while line := next(f).strip():
            x, y = line.split(',')
            dots.add((int(x), int(y)))
        
        while line := next(f).strip():
            coord, val = line.removeprefix("fold along ").split("=")
            ops.append((coord, int(val)))
    except StopIteration:
        pass

op = ops[0]
for x, y in list(dots):
    if op[0] == 'x':
        if x < op[1]:
            pass
        else:
            dots.remove((x, y))
            nx = op[1] - (x - op[1])
            if nx >= 0 and (nx, y) not in dots:
                dots.add((nx, y))
    else:
        if y < op[1]:
            pass
        else:
            dots.remove((x, y))
            ny = op[1] - (y - op[1])
            if ny >= 0 and (x, ny) not in dots:
                dots.add((x, ny))

print(len(dots))