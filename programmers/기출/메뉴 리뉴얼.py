# 2021 KAKAO BLIND RECRUITMENT / 메뉴 리뉴얼
# https://school.programmers.co.kr/learn/courses/30/lessons/72411
from collections import defaultdict
from itertools import combinations
def solution(orders, course):
    answer = []
    courses = defaultdict(int)
    for order in orders:
        for cour in course:
            for case in combinations(order, cour):
                # print(''.join(sorted(case)))
                courses[''.join(sorted(case))] += 1
    aa = sorted(courses.items(), key=lambda x: -x[1])
    max_cnt = [0 for _ in course]
    for a in aa:
        for idx, cour in enumerate(course):
            if len(a[0]) == cour:
                max_cnt[idx] = max(max_cnt[idx], a[1])
                if a[1] == max_cnt[idx] and max_cnt[idx] > 1:
                    answer.append(a[0])
                
    return sorted(answer)