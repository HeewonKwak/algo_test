# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer = -1
    stack = []
    for i in s:
        if len(stack) >= 1:
            if stack[-1] == i:
                stack.pop()
                continue
        stack.append(i)
    if len(stack) == 0:
        return 1
    return 0