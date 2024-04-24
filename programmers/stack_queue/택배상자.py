# https://school.programmers.co.kr/learn/courses/30/lessons/131704
from collections import deque
def solution(order):
    answer = 0
    q = deque([i for i in range(1, len(order)+1)])
    qq = []
    idx = 0
    while q or qq:
        # print(idx, q, qq)
        if len(q) == 0:
            if order[idx] == qq.pop():
                answer += 1
                idx += 1
            else:
                break
        elif len(qq) == 0:
            box = q.popleft()
            if order[idx] == box:
                answer += 1
                idx += 1
            else:
                qq.append(box)
        else:
            if qq[-1] == order[idx]:
                qq.pop()
                answer += 1
                idx += 1
            elif q[0] == order[idx]:
                q.popleft()
                answer += 1
                idx += 1
            else:
                qq.append(q.popleft())
            
    return answer