# https://school.programmers.co.kr/learn/courses/30/lessons/12914
import math
def solution(n):
    answer = 0
    one = n
    two = 0
    # print(help(math))
    while(1):
        if one == n or one == 0:
            answer += 1
        else:
            answer += math.factorial(one+two) // (math.factorial(one)*math.factorial(two))
        if one == 0 or one == 1:
            break
        one -= 2
        two += 1
    return answer%1234567