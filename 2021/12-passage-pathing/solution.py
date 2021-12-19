edges = {}

with open('input2.txt', 'r') as f:
    for line in f:
        u, v = line.strip().split("-")
        if u not in edges:
            edges[u] = []
        if v not in edges:
            edges[v] = []
        edges[u].append(v)
        edges[v].append(u)

ans = 0

def dfs(s: str, visited_sm: set[int]):
    global ans
    if s == 'end':
        ans += 1
        return
    
    can_go: list[str] = edges[s]
    for v in can_go:
        if v.isupper():
            dfs(v, visited_sm)
        elif v not in visited_sm and v != 'start':
            visited_sm.add(v)
            dfs(v, visited_sm)
            visited_sm.remove(v)

dfs('start', set())
print(ans)