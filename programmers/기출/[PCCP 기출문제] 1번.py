# PCCP 기출문제 / [PCCP 기출문제] 1번
# https://school.programmers.co.kr/learn/courses/30/lessons/250137
from collections import deque
def solution(bandage, health, attacks):
    answer = 0
    max_health = health
    time = 0
    end_time = attacks[-1][0]
    heal_time = 0
    attacks = deque(attacks)
    while time <= end_time:
        if attacks[0][0] == time:
            _, damage = attacks.popleft()
            health -= damage
            if health <= 0:
                return -1
            heal_time = 0
        else:
            health = min(health + bandage[1], max_health)
        if heal_time == bandage[0]:
            health = min(health + bandage[2], max_health)
            heal_time = 0
        time += 1
        heal_time += 1
    return health