import sys

x1, y1, x2, y2 = map(int, sys.argv[1:5])

# find min/max Vxo, when Vto is 0, need to at least reach target area left border
Vxo_min = 1
while (Vxo_min+1)*Vxo_min/2 < x1-1:
    Vxo_min += 1

Vxo_max = x2

print(f"{Vxo_min=} {Vxo_max=}")

# for Vxo in range(Vxo_min, Vxo_min+1):
    # for Vyo in range(3, 4):
valid_vos_count = 0
for Vxo in range(Vxo_min, Vxo_max+1):
    for Vyo in range(y1, 1000):
        vxt = Vxo
        vyt = Vyo
        pos_x = 0
        pos_y = 0
        while True:
            pos_x += vxt
            pos_y += vyt
            vxt = max(vxt-1, 0)
            vyt -= 1
            
            if x1 <= pos_x <= x2 and y1 <= pos_y <= y2:
                # print(f"{Vxo=}, {Vyo=}")
                valid_vos_count += 1
                break
            
            if pos_y < y1:
                break

print(valid_vos_count)