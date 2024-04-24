# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    case = find_rc(yellow)
    area = brown + yellow
    for row, col in case:
        if (row + 2 ) * (col + 2) == area:
            return [col + 2, row + 2]

def find_rc(area):
    rc = []
    for i in range(1, int(pow(area, 0.5)) + 1):
        if area % i == 0:
            rc.append([i, area//i])
    return rc