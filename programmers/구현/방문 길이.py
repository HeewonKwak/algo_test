# Summer/Winter Coding(~2018) / 방문 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/49994#
def solution(dirs):
    answer = 0
    now = [0, 0]
    all_case = []
    for i in dirs:
        past = now.copy()
        if i == 'U' and now[1] + 1 <= 5:
            now[1] += 1
        elif i == 'D' and now[1] - 1 >= -5:
            now[1] -= 1
        elif i == 'R' and now[0] + 1 <= 5:
            now[0] += 1
        elif i == 'L' and now[0] - 1 >= -5:
            now[0] -= 1
        if [past, now] not in all_case and past != now:
            answer += 1
            all_case.append([past.copy(), now.copy()])
            all_case.append([now.copy(), past.copy()])
    return answer