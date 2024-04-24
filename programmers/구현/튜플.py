# https://school.programmers.co.kr/learn/courses/30/lessons/64065
from collections import defaultdict

def solution(s):
    answer = []
    x = s.split(',')
    ss = []
    for i in x:
        ii = ''
        for j in i:
            if j != '{' and j != '}':
                ii += j
        ss.append(int(ii))
    dd = defaultdict(int)
    for i in ss:
        dd[i] += 1
    dd = sorted(dd.items(), key=lambda x: x[1], reverse=True)
    for i in dd:
        answer.append(i[0])
    return answer