# https://school.programmers.co.kr/learn/courses/30/lessons/135807
import math

def solution(arrayA, arrayB):
    answer = 0
    arrayA.sort()
    arrayB.sort()
    num1 = arrayA[0]
    for a in arrayA:
        num1 = gcd(num1, a)
    if num1 != 1:
        div = divisor(num1)
        for b in arrayB:
            div2 = []
            for d in div:
                if b % d != 0:
                    div2.append(d)
            div = div2
            if not div:
                num1 = 0
                break
            num1 = div[-1]
    else:
        num1 = 0
    num2 = arrayB[0]
    for a in arrayB:
        num2 = gcd(num2, a)
    if num2 != 1:
        div = divisor(num2)
        for b in arrayA:
            div2 = []
            for d in div:
                if b % d != 0:
                    div2.append(d)
            div = div2
            if not div:
                num2 = 0
                break
            num2 = div[-1]
    else:
        num2 = 0
    answer = max(num1, num2)
    return answer

def gcd(a, b):
    if b % a == 0:
        return a
    num = 1
    for i in range(2, a//2 + 1):
        if b % i == 0 and a % i == 0:
            num = i
    return num

def divisor(num):
    div = []
    for i in range(2, num//2 + 1):
        if num % i == 0:
            div.append(num)
    div.append(num)
    return div