# 2018 KAKAO BLIND RECRUITMENT / [1차] 프렌즈4블록
# https://school.programmers.co.kr/learn/courses/30/lessons/17679#
def solution(m, n, board):
    answer = 0
    while 1:
        check = 0 # check delete
        delete = [[False if board[y][x] != '@' else True for x in range(n)] for y in range(m)]
        for y in range(m):
            board[y] = list(board[y])
        for y in range(m-1):
            for x in range(n-1):
                check += find_two_two(board, x, y, delete)
        if check == 0:
            break
        for y in range(m-1, -1, -1):
            for x in range(n):
                if delete[y][x] == True:
                    board[y][x] = '@'
        for y in range(m-2, -1, -1):
            for x in range(n):
                if board[y+1][x] == '@' and board[y][x] != '@':
                    for yy in range(y+1, m):
                        if board[yy][x] != '@':
                            board[yy-1][x] = board[y][x]
                            board[y][x] = '@'
                            break
                    else:
                        board[m-1][x] = board[y][x]
                        board[y][x] = '@'
    for y in range(m):
        for x in range(n):
            if board[y][x] == '@':
                answer += 1
    return answer

def find_two_two(board, x, y, delete):
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    check = board[y][x]
    if check == '@':
        return 0
    for i in range(3):
        xx = x + dx[i]
        yy = y + dy[i]
        if board[yy][xx] != check:
            return 0
    delete[y][x] = True
    for i in range(3):
        xx = x + dx[i]
        yy = y + dy[i]
        delete[yy][xx] = True
    return 1