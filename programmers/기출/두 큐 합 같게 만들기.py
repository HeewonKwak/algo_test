# 2022 KAKAO TECH INTERNSHIP / 두 큐 합 같게 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque
def solution(queue1, queue2):
    target = (sum(queue1 + queue2)) // 2
    if sum(queue1) == target:
        return 0
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    qs1 = sum(q1)
    qs2 = sum(q2)
    while(1):
        if qs1 > target:
            move = q1.popleft()
            q2.append(move)
            qs1 = qs1 - move
            qs2 = qs2 + move
        elif qs1 < target:
            move = q2.popleft()
            q1.append(move)
            qs1 = qs1 + move
            qs2 = qs2 - move
        else:
            return answer
        answer += 1
        if qs1 == 0 or qs2 == 0 or answer > 600000:
            return -1
    return answer
