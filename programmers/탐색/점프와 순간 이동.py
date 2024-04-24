# https://school.programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    ans = 0
    while(1):
        n, a = n//2, n%2
        ans += a
        if n == 0:
            break
    return ans