# https://school.programmers.co.kr/learn/courses/30/lessons/17687
def solution(n, t, m, p):
    answer = ''
    nums = ''
    # print(nth(10, n))
    for i in range(0, m*t + 1):
        nums += nth(i, n)
    for idx, i in enumerate(nums):
        if idx % m == p - 1:
            answer += i
        if len(answer) == t:
            break
    return answer

def nth(num, n):
    nn = ""
    mod = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while(1):
        num, a = num // n, mod[num % n]
        nn += a
        if num == 0:
            break
    return nn[::-1]