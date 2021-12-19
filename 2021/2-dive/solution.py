hor = 0
depth = 0
aim = 0

for line in open("input.txt", "r"):
    dir, val = line.split(" ", 1)
    val = int(val)
    if dir.startswith("f"):
        hor += val
        depth += aim * val
    elif dir.startswith("u"):
        aim -= val
        # depth -= val
    else:
        aim += val
        # depth += val
    
print(hor * depth)