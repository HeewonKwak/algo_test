# 탐욕법(Greedy) / 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885#
from collections import Counter
import math
def solution(people, limit):
    answer = 0
    kg = Counter(people)
    kg_key = sorted(kg.keys(), reverse=True)
    start = 0
    end = len(kg_key) - 1
    while(start <= end):
        if kg_key[start] + kg_key[end] > limit:
            answer += kg[kg_key[start]]
            start += 1
        elif start == end:
            answer += math.ceil(kg[kg_key[start]]/2)
            start += 1
        elif kg_key[start] + kg_key[end] <= limit:
            if kg[kg_key[start]] > kg[kg_key[end]]:
                answer += kg[kg_key[end]]
                kg[kg_key[start]] -= kg[kg_key[end]]
                end -= 1
            elif kg[kg_key[start]] == kg[kg_key[end]]:
                answer += kg[kg_key[end]]
                start += 1
                end -= 1
            else:
                answer += kg[kg_key[start]]
                kg[kg_key[end]] -= kg[kg_key[start]]
                start += 1
            
    return answer

# 복습
def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people)-1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        answer += 1
    return answer