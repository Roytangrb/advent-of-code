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

def dfs(s: str, visited_sm: set[int], twice: bool):
    global ans
    if s == 'end':
        ans += 1
        return
    
    can_go: list[str] = edges[s]
    for v in can_go:
        if v == 'start':
            continue
        if v.isupper():
            dfs(v, visited_sm, twice)
        else:
            if v not in visited_sm:
                visited_sm.add(v)
                dfs(v, visited_sm, twice)
                visited_sm.remove(v)
            elif not twice:
                dfs(v, visited_sm, True)
            
dfs('start', set(), False)
print(ans)