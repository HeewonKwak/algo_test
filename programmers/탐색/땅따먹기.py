# 탐색 / 땅따먹기
# https://school.programmers.co.kr/learn/courses/30/lessons/1880
def solution(land):
    answer = []
    for i in land:
        if answer == []:
            answer = i
        else:
            answer[0], answer[1], answer[2], answer[3] = i[0] + max(answer[1], answer[2], answer[3]), i[1] + max(answer[0], answer[2], answer[3]), i[2] + max(answer[1], answer[0], answer[3]), i[3] + max(answer[1], answer[2], answer[0])
    return max(answer)