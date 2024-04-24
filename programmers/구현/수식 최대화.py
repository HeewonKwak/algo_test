# https://school.programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations

def solution(expression):
    answer = 0
    origin_num, operator = operator_split(expression)
    for i in permutations(operator, len(operator)):
        answer = max(priority(origin_num.copy(), i), answer)

    return answer

def priority(num, operator):
    cal_num = []
    for i in operator:
        idx = 0
        while(1):
            if idx == len(num) - 1:
                cal_num.append(num[idx])
                break
            if num[idx + 1] == i:
                num[idx+2] = cal(num[idx], num[idx+1], num[idx+2])
                idx += 2
            else:
                cal_num.append(num[idx])
                idx += 1
        num = cal_num
        cal_num = []
    return abs(num[0])

def cal(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op =='*':
        return num1 * num2

def operator_split(expression):
    split_list = []
    operator_list = set()
    check = 0
    for i in range(len(expression)):
        if expression[i] in ['-', '+', '*']:
            split_list.append(int(expression[check:i]))
            split_list.append(expression[i])
            operator_list.add(expression[i])
            check = i + 1
    split_list.append(int(expression[check:]))
    return split_list, operator_list