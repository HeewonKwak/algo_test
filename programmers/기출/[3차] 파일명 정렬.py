# 2018 KAKAO BLIND RECRUITMENT / [3차] 파일명 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/17686
from collections import defaultdict
import re
def solution(files):
    answer = []
    names = defaultdict(list)
    for file in files:
        ff = re.split(r'(\d+)', file)
        head, number = ff[0], ff[1]
        names[file] = [head.lower(), int(number)]
    for name in sorted(names.items(), key=lambda x: (x[1][0], x[1][1])):
        answer.append(name[0])
    return answer