# 2018 KAKAO BLIND RECRUITMENT / [3차] 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/17684
def solution(msg):
    answer = []
    lzw = dict()
    for i in range(1, 27):
        lzw[chr(i+64)] = i
    idx = 1
    start = 0
    next_num = 27
    while start <= len(msg)-1:
        if msg[start:idx] in lzw.keys() and idx == len(msg):
            answer.append(lzw[msg[start:idx]])
            return answer
        elif msg[start:idx] not in lzw.keys():
            lzw[msg[start:idx]] = next_num
            next_num += 1
            answer.append(lzw[msg[start:idx-1]])
            start = idx - 1
            idx = start + 1
            continue
        idx += 1
        
    return answer