# https://school.programmers.co.kr/learn/courses/30/lessons/42889

from collections import Counter
def solution(N, stages):
    answer = []
    sc = Counter(stages)
    all_sum = 0
    if N + 1 in stages:
        all_sum += sc[N+1]
    ss = []
    for i in range(N, 0, -1):
        if i in stages:
            all_sum += sc[i]
        if all_sum == 0:
            ss.append([0, i])
        else:
            ss.append([sc[i] / all_sum, i])
    # print(ss)
    ss = sorted(ss, key=lambda x: [x[0], -x[1]], reverse=True)
    answer = [x for _, x in ss]
    return answer