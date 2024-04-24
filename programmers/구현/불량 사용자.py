# https://school.programmers.co.kr/learn/courses/30/lessons/64064
from collections import defaultdict

def solution(user_id, banned_id):
    cc = []
    case = defaultdict(list)
    for index, i in enumerate(banned_id):
        for j in user_id:
            if len(i) != len(j):
                continue
            for k in range(len(i)):
                if i[k] == '*' or i[k] == j[k]:
                    continue
                else:
                    break
            else:
                case[index].append(j)
    def dfs(case, step, check, cc):
        if step == len(case):
            cc.append(check)
            return
        for i in case[step]:
            if i in check:
                continue
            else:
                dfs(case, step + 1, check + [i], cc)
    dfs(case, 0, [], cc)
    for i in range(len(cc)):
        cc[i] = sorted(cc[i])
    answer = []
    for i in cc:
        if i not in answer:
            answer.append(i)
    return len(answer)