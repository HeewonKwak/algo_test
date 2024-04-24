from collections import deque

def solution(board):
    answer = 1
    visited = [[0 if board[i][j]=='.' else -1 for j in range(len(board[0]))] for i in range(len(board))]
    check = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='R':
                si = i
                sj = j
                check = True
                break
        if check:
            break
    queue = deque()
    queue.append([si, sj])
    visited[si][sj] = 0
    while(len(queue)):
        a, b = queue.popleft()
        dx = 1
        while(1):
            if b == len(board[0]) - 1 or board[a][b + dx] == 'D':
                break
            if b + dx + 1 == len(board[0]):
                if board[a][b + dx] == 'G':
                    return visited[a][b] + 1
                elif visited[a][b + dx] == 0:
                    queue.append([a, b+dx])
                    visited[a][b + dx] = visited[a][b] + 1
                break
            if board[a][b + dx + 1] == 'D':
                if board[a][b + dx] == 'G':
                    return visited[a][b] + 1
                elif visited[a][b + dx] == 0:
                    queue.append([a, b+dx])
                    visited[a][b + dx] =  visited[a][b] + 1
                break
            dx += 1
        dx = -1
        while(1):
            if b == 0 or board[a][b + dx] == 'D':
                break
            if b + dx - 1 == -1:
                if board[a][b + dx] == 'G':
                    return visited[a][b] + 1
                elif visited[a][b + dx] == 0:
                    queue.append([a, b+dx])
                    visited[a][b + dx] = visited[a][b] + 1
                break
            if board[a][b + dx - 1] == 'D':
                if board[a][b + dx] == 'G':
                    return visited[a][b] + 1
                elif visited[a][b + dx] == 0:
                    queue.append([a, b+dx])
                    visited[a][b + dx] = visited[a][b] + 1
                break
            dx += -1
        dy = -1
        while(1):
            if a == 0 or board[a+dy][b] == 'D':
                break
            if a + dy - 1 == -1:
                if board[a+dy][b] == 'G':
                    return visited[a][b] + 1
                elif visited[a+dy][b] == 0:
                    queue.append([a + dy, b])
                    visited[a+dy][b] = visited[a][b] + 1
                break
            if board[a+ dy - 1][b] == 'D':
                if board[a + dy][b] == 'G':
                    return visited[a][b] + 1
                elif visited[a+dy][b] == 0:
                    queue.append([a + dy, b])
                    visited[a+dy][b] = visited[a][b] + 1
                break
            dy += -1
        dy = 1
        while(1):
            if a == len(board) - 1 or board[a+dy][b] == 'D':
                break
            if a + dy + 1 == len(board):
                if board[a+dy][b] == 'G':
                    return visited[a][b] + 1
                elif visited[a+dy][b] == 0:
                    queue.append([a + dy, b])
                    visited[a+dy][b] = visited[a][b] + 1
                break
            if board[a+ dy + 1][b] == 'D':
                if board[a + dy][b] == 'G':
                    return visited[a][b] + 1
                elif visited[a+dy][b] == 0:
                    queue.append([a + dy, b])
                    visited[a+dy][b] = visited[a][b] + 1
                break
            dy += 1
        answer += 1
    # print(visited)
    return -1