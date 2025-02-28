def solution(board, h, w):
    n = len(board)
    count = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    for i in range(4):
        check_h = h + dh[i]
        check_w = w + dw[i]
        if (0 <= check_h < n) and (0 <= check_w < n):
            if board[h][w] == board[check_h][check_w]:
                count += 1
    return count