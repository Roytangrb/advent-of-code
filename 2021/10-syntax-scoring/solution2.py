from collections import deque
from statistics import median

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

comps = []
with open('input2.txt', 'r') as f:
    for line in f:
        st = deque()
        corrupted = False
        for ch in line.strip():
            if ch in pairs:
                st.append(ch)
            else:
                top_ch = st.pop()
                if ch != pairs[top_ch]:  # corrupted
                    corrupted = True
                    break
        if st and not corrupted:  # incomplete
            comp_score = 0
            while st:
                end_ch = pairs[st.pop()]
                comp_score = comp_score * 5 + scores[end_ch]
            comps.append(comp_score)

                    
print(median(comps))