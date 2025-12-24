def is_valid(board):
    VALID = set(range(1, 10))
    starts = [(r, c) for r in (0, 3, 6) for c in (0, 3, 6)]

    # rows
    if any(set(row) != VALID for row in board):
        return 0

    # cols
    if any({board[r][c] for r in range(9)} != VALID for c in range(9)):
        return 0

    # boxes
    for sr, sc in starts:
        if {board[r][c] for r in range(sr, sr+3) for c in range(sc, sc+3)} != VALID:
            return 0

    return 1


T = int(input())
for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    print(f"#{tc} {is_valid(board)}")
