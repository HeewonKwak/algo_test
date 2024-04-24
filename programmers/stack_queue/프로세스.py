# https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0
    pd = []
    for i in range(len(priorities)):
        pd.append([priorities[i], i])
    queue = deque(pd)
    # print(priorities)
    while(len(queue)):
        p, l = queue.popleft()
        # print(p, l, priorities)
        if p != max(priorities):
            queue.append([p, l])
        else:
            answer += 1
            priorities.remove(p)
            if l == location:
                return answer
        
    return answer