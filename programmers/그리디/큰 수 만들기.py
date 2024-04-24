# 탐욕법(Greedy) / 큰 수 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/42883#
from collections import deque
def solution(number, k):
    answer = ''
    nn = len(number) - k
    q = deque(number[k+1:])
    check_q = deque(number[:k+1])
    while len(answer) < nn:
        if len(check_q) != 0:
            max_idx = find_max_index(check_q)
            answer += check_q[max_idx]
            k -= max_idx
        if k == 0:
            answer += ''.join(q)
            q.clear()
        for _ in range(max_idx+1):
            if len(check_q) == 0:
                break
            check_q.popleft()
        for i in range(k+1 - len(check_q)):
            if len(q) == 0:
                break
            num = q.popleft()
            check_q.append(num)
        if len(check_q) == k:
            k = 0
            check_q.clear()
    return answer

def find_max_index(queue):
    max_num = '0'
    max_idx = 0
    for i in range(len(queue)):
        if queue[i] == '9':
            return i
        if queue[i] > max_num:
            max_num = queue[i]
            max_idx = i
    return max_idx

print(solution('4321', 1))