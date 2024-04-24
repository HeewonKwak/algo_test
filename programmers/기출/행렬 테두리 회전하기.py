# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) / 행렬 테두리 회전하기(구현)
# https://school.programmers.co.kr/learn/courses/30/lessons/77485
def print_array(arr):
    if len(arr) > 10:
        return
    for a in arr:
        print(a)

def solution(rows, columns, queries):
    answer = []
    array = [[i*columns + j + 1 for j in range(columns)] for i in range(rows)]
    # print_array(array)
    for x1, y1, x2, y2 in queries:
        min_val = float('INF')
        point = array[x1-1][y1-1]
        min_val = min(min_val, point)
        for x in range(x1-1, x2-1):
            min_val = min(min_val, array[x+1][y1 - 1])
            array[x][y1 - 1] = array[x+1][y1 - 1]
        for y in range(y1-1, y2-1):
            min_val = min(min_val, array[x2-1][y + 1])
            array[x2-1][y] = array[x2-1][y + 1]
        for x in range(x2 - 1, x1-1, -1):
            min_val = min(min_val, array[x-1][y2 - 1])
            array[x][y2 - 1] = array[x-1][y2 - 1]
        for y in range(y2 - 1, y1-1, -1):
            min_val = min(min_val, array[x1-1][y - 1])
            array[x1-1][y] = array[x1-1][y - 1]
        array[x1-1][y1] = point
        answer.append(min_val)
        # print(point)
        # print_array(array)
    return answer