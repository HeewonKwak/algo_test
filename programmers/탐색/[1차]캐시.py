# https://school.programmers.co.kr/learn/courses/30/lessons/17680
def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in cities:
        city = i.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        elif len(cache) < cacheSize:
            cache.append(city)
            answer += 5
        elif cacheSize == 0:
            answer += 5
        else:
            cache.pop(0)
            cache.append(city)
            answer += 5
    return answer