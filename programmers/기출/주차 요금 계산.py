# 2022 KAKAO BLIND RECRUITMENT / 주차 요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341
from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    cars = defaultdict(list)
    car_time = defaultdict(int)
    car_out = []
    for record in records:
        time, car_num, state = record.split()
        car_out.append(car_num)
        h, m = time.split(':')
        if state == 'IN':
            cars[car_num].append([h, m])
        else:
            lh, lm = cars[car_num].pop()
            car_time[car_num] += (int(h)-int(lh)) * 60 + (int(m)-int(lm))
    for car in cars.keys():
        if len(cars[car]) != 0:
            lh, lm = cars[car].pop()
            car_time[car] += (23-int(lh)) * 60 + (59-int(lm))
    car_set = sorted(set(car_out))
    for car_num in car_set:
        time = car_time[car_num]
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3])
    return answer