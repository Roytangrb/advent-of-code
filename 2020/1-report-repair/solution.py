target = 2020
comp = set()

for line in open('input.txt', 'r'):
    num = int(line)
    if num in comp:
        print(num, target - num)
        print(num * (target - num))
        break
    else:
        comp.add(target - num)