# https://school.programmers.co.kr/learn/courses/30/lessons/120866

from collections import Counter
def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                make_bomb(board, i, j)
    for i in board:
        cc = Counter(i)
        answer += cc[0]
    return answer

def make_bomb(board, x, y):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        if x + dx[i] < 0 or y + dy[i] < 0 or x + dx[i] >=len(board) or y + dy[i] >= len(board):
            continue
        elif board[x + dx[i]][y + dy[i]] == 1:
            continue
        else:
            board[x + dx[i]][y + dy[i]] = 2