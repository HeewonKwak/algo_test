# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0
    score = []
    check = False
    for idx, i in enumerate(dartResult):
        if check:
            check = False
            continue
        if i.isdigit():
            if dartResult[idx+1] == '0':
                check = True
                score.append(10)
            else:
                score.append(int(i))
        elif i == 'D':
            score[-1] = pow(score[-1], 2)
        elif i == 'T':
            score[-1] = pow(score[-1], 3)
        elif i == "*":
            if len(score) == 1:
                score[0] = score[0] * 2
            else:
                score[-1] = score[-1] * 2
                score[-2] = score[-2] * 2
        elif i == "#":
            score[-1] = score[-1] * -1
    print(score)
    return sum(score)