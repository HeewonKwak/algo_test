# 탐욕법(Greedy) / 조이스틱
# https://school.programmers.co.kr/learn/courses/30/lessons/42860#
def updown(num):
    return min((num - 65), abs(91-num))

def solution(name):
    answer = 0
    for i in range (len(name)):
        answer += updown(ord(name[i]))
    n = len(name)
    name_num = []
    target = [i for i in range(len(name)) if name[i] == 'A' and i != 0]
    a_idx = []
    for i, j in enumerate(target):
        if not a_idx:
            a_idx.append([j, j])
        elif a_idx[-1][1] + 1 == j:
            a_idx[-1][1] += 1
        else:
            a_idx.append([j, j])
    move = n - 1
    for start, end in a_idx:
        case = min(start - 1, n - end - 1) * 2 + max(start - 1, n - end - 1)
        case = max(case, 0)
        move = min(move, case)
    answer += move
    return answer