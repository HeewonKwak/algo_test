# https://school.programmers.co.kr/learn/courses/30/lessons/120871
def solution(n):
    answer = 0
    no3 = []
    i = 1
    while(1):
        if len(no3) == n:
            return no3[n - 1]
        if check3(i) and i%3 != 0:
            no3.append(i)
        i += 1
    return answer

def check3(num):
    a = str(num)
    for ii in a:
        if ii == '3':
            return False
    return True