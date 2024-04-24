# https://school.programmers.co.kr/learn/courses/30/lessons/76502
def solution(s):
    answer = 0
    if len(s) % 2 == 1:
        return 0
    for i in range(len(s)):
        ss = s[i:] + s[:i]
        # print(ss, check(ss))
        if check(ss):
            answer += 1
    return answer

def check(ss):
    a1 = 0
    a2 = 0
    a3 = 0
    back = []
    for i in ss:
        if i == "(":
            a1 += 1
            back.append(")")
        elif i == "[":
            a2 += 1
            back.append("]")
        elif i == "{":
            a3 += 1
            back.append("}")
        if len(back) == 0:
            return False
        if i == ")":
            a1 -= 1
            if back.pop() != ")":
                return False
        elif i == "]":
            a2 -= 1
            if back.pop() != "]":
                return False
        elif i == "}":
            a3 -= 1
            if back.pop() != "}":
                return False
        if a1 < 0 or a2 < 0 or a3 < 0:
            return False
    if a1 == 0 and a2 == 0 and a3 == 0:
        return True
    else:
        return False