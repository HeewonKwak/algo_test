# 2020 카카오 인턴십 / 보석 쇼핑
# https://school.programmers.co.kr/learn/courses/30/lessons/67258
from collections import defaultdict
def solution(gems):
    uniqe = set(gems)
    answer = [0, len(uniqe)]
    start = 0
    end = len(uniqe)
    gem = defaultdict(int)
    check = len(gems) + 1
    for gg in gems[:end]:
        gem[gg] += 1
    while 1:
        if len(gem.keys()) == len(uniqe) and gem[gems[start]] == 1:
            if end - start < check:
                answer[0] = start + 1
                answer[1] = end
                if end - start == len(uniqe):
                    break
                check = end - start
            if start + len(uniqe) > len(gems):
                break
            gem[gems[start]] -= 1
            if gem[gems[start]] == 0:
                gem.pop(gems[start])
            start += 1
            if end >= len(gems):
                break
            gem[gems[end]] += 1
            end += 1
        elif len(gem.keys()) >= len(uniqe):
            gem[gems[start]] -= 1
            if gem[gems[start]] == 0:
                gem.pop(gems[start])
            start += 1
        elif end >= len(gems):
            break
        elif len(gem.keys()) < len(uniqe):
            gem[gems[end]] += 1
            end += 1
        else:
            gem[gems[start]] -= 1
            if gem[gems[start]] == 0:
                gem.pop(gems[start])
            start += 1
    return answer