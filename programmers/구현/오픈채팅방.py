# https://school.programmers.co.kr/learn/courses/30/lessons/42888
from collections import defaultdict

def solution(record):
    answer = []
    xx = []
    uid = defaultdict(str)
    for i in record:
        rr = list(i.split())
        if rr[0] == 'Enter':
            xx.append([rr[1], '님이 들어왔습니다.'])
            uid[rr[1]] = rr[2]
        elif rr[0] == 'Leave':
            xx.append([rr[1], '님이 나갔습니다.'])
        else:
            uid[rr[1]] = rr[2]
    for i in xx:
        answer.append(uid[i[0]]+i[1])
    return answer