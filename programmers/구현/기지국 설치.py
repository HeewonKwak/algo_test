# https://school.programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):
    answer = 0
    first = [x - w for x in stations] + [n+1]
    end = [0] + [x + w for x in stations]
    areas = []
    for i in range(len(first)):
        if first[i] - end[i] > 0:
            areas.append(first[i] - end[i] - 1)
    for i in areas:
        answer += i // (2*w +1)
        if i % (2*w +1) > 0:
            answer += 1
    return answer