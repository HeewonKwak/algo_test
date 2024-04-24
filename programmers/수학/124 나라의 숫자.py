# 124 나라의 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12899#
def solution(n):
    answer = ''
    n -= 1
    check = False
    while n > 0:
        n, a = n // 3, n % 3
        if a == 0 and check:
            answer += '4'
            n -= 1
        elif not check:
            if a == 2:
                answer += '4'
            else:
                answer += str(a + 1)
        else:
            answer += str(a)
        check = True
    return answer[::-1]