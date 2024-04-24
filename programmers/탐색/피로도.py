# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations
def solution(k, dungeons):
    answer = -1
    # print(help(permutations))
    for i in permutations(dungeons,len(dungeons)):
        tired = k
        cnt = 0
        for min_tired, need_tired in i:
            if min_tired <= tired:
                tired -= need_tired
                cnt += 1
        answer = max(answer, cnt)
                
    return answer