# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 0

    people = [i for i in range(1, n+1)]
    people[a - 1] = "A"
    people[b - 1] = "B"
    while(1):
        nb = []
        idx = 0
        answer += 1
        while(1):
            if people[idx] in ['A', 'B'] and people[idx + 1] in ['A', 'B']:
                return answer
            elif people[idx] in ['A', 'B']:
                nb.append(people[idx])
            elif people[idx + 1] in ['A', 'B']:
                nb.append(people[idx + 1])
            else:
                nb.append(people[idx])
            idx += 2
            if idx == len(people):
                break
        people = nb.copy()

    return answer