# 2022 KAKAO TECH INTERNSHIP / 성격 유형 검사하기
# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    answer = ''
    p_types = ["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"]
    scores = [0, 0, 0, 0] # R, F, M, A
    for p_type, choice in zip(survey, choices):
        pp = p_types.index(p_type)
        if pp % 2 == 0:
            scores[pp//2] += 4 - choice
        else:
            scores[pp//2] += choice - 4
    if scores[0] >= 0:
        answer += 'R'
    else:
        answer += 'T'
    if scores[1] > 0:
        answer += 'F'
    else:
        answer += 'C'
    if scores[2] > 0:
        answer += 'M'
    else:
        answer += 'J'
    if scores[3] >= 0:
        answer += 'A'
    else:
        answer += 'N'
    return answer