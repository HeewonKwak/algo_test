# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    
    a = 0
    b = 0
    for i in s:
        if i =='(':
            a += 1
        else:
            b += 1
        if b > a:
            return False
    if a != b:
        return False
    return True