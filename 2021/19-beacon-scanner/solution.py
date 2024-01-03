import sys

scanners: list[list[tuple[int, int, int]]] = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        if line.startswith('---'):
            scanners.append([])
            continue
        if not line.strip():
            continue
        beacon = tuple(map(int, line.strip().split(',')))
        scanners[-1].append(beacon)
