# 2023 KAKAO BLIND RECRUITMENT / 이모티콘 할인행사 / 탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    sale = [0.6, 0.7, 0.8, 0.9]
    for ratio in product(*(sale for _ in range(len(emoticons)))):
        plus_cnt, total_money = find_ratio(users, ratio, emoticons)
        if answer[0] < plus_cnt:
            answer = [plus_cnt, total_money]
        elif answer[0] == plus_cnt:
            answer[1] = max(answer[1], total_money)
    
    return answer

def find_ratio(users, ratio, emoticons):
    plus = 0
    total_money = 0
    for persent, cut in users:
        money = 0
        for i in range(len(ratio)):
            if ratio[i] <= (100-persent)/100:
                money += emoticons[i] * ratio[i]
            if money >= cut:
                plus += 1
                money = 0
                break
        total_money += money
    return plus, int(total_money)