from collections import deque

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

ans1 = 0
with open('input2.txt', 'r') as f:
    for line in f:
        st = deque()
        for ch in line.strip():
            if ch in pairs:
                st.append(ch)
            else:
                top_ch = st[-1]
                if ch != pairs[top_ch]:  # corrupted
                    score = scores[ch]
                    ans1 += score
                    break
                else:
                    st.pop()
                    
print(ans1)