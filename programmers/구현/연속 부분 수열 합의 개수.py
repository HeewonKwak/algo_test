# https://school.programmers.co.kr/learn/courses/30/lessons/131701
def solution(elements):
    answer = 0
    el = len(elements)
    elements = elements + elements[:-1]
    case = set()
    for i in range(1, el+1):
        for j in range(el):
            # print(elements[j:j+i])
            case.add(sum(elements[j:j+i]))
    # print(case)
    return len(case)