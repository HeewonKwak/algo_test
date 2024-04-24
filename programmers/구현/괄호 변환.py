# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    answer = ''
    answer = check(p, answer)
    return answer

def check(parentheses, answer):
    if parentheses == '':
        return ''
    open_parentheses = 0
    close_parentheses = 0
    parentheses1 = ""
    parentheses2 = ""
    ch1 = True
    ch2 = True
    ch3 = True
    ch4 = False
    for idx, i in enumerate(parentheses):
        if i == "(":
            open_parentheses += 1
        else:
            close_parentheses += 1
        if open_parentheses < close_parentheses:
            ch2 = False
        if ch1:
            parentheses1 += i
        else:
            parentheses2 += i
        if open_parentheses == close_parentheses:
            if not ch2:
                ch3 = False
            elif ch3:
                ch4 = True
            ch1 = False
    if ch2:
        return parentheses1 + parentheses2
    elif ch4:
        return parentheses1 + check(parentheses2, answer)
    else:
        return change(parentheses1, parentheses2, answer)

def change(u, v, answer):
    uu = "("
    a = check(v, answer)
    uu += a
    uu += ")"
    for i in u[1:-1]:
        if i == "(":
            uu += ")"
        else:
            uu += "("
    return answer + uu
    