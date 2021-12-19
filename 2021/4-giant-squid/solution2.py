nums = []

boards = []

for i, line in enumerate(open('input2.txt', 'r')):
    if i == 0:
        nums = [int(d) for d in line.strip().split(',')]
        continue
    if not line.strip():
        boards.append([])
    else:
        boards[-1].append([int(v) for v in line.strip().split() if v is not None])


boards_win_at = [-1] * len(boards)
row_count = [[0] * 5 for _ in range(len(boards))]
col_count = [[0] * 5 for _ in range(len(boards))]

def mark(i, num):
    for bi, board in enumerate(boards):    
        for r in range(5):
            for c in range(5):
                if board[r][c] == num:
                    board[r][c] = -1
                    row_count[bi][r] -= 1
                    col_count[bi][c] -= 1
                    
                    if any([count == -5 for count in row_count[bi]]) or any([count == -5 for count in col_count[bi]]):
                        if boards_win_at[bi] == -1:
                            boards_win_at[bi] = i
                        
                        if all([won_at != -1 for won_at in boards_win_at]):
                            return True
    return False

for i, num in enumerate(nums):
    if mark(i, num):
        break

last_won_bi = -1
last_won_ni = -1
for bi, ni in enumerate(boards_win_at):
    if ni > last_won_ni:
        last_won_ni = ni
        last_won_bi = bi

not_marked = 0
eb = boards[last_won_bi]
for r in range(5):
    for c in range(5):
        if eb[r][c] != -1:
            not_marked += eb[r][c]

print(not_marked * nums[last_won_ni])