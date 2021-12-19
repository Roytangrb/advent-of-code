nums = []

boards = []

for i, line in enumerate(open('input.txt', 'r')):
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
                        boards_win_at[bi] = i
                        return bi
    return -1

end_i = None
end_num = None
for i, num in enumerate(nums):
    if (bei := mark(i, num)) >= 0:
        end_i = bei
        end_num = num
        break

not_marked = 0
eb = boards[end_i]
for r in range(5):
    for c in range(5):
        if eb[r][c] != -1:
            not_marked += eb[r][c]

print(not_marked * end_num)