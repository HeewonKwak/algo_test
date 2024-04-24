# 코딩테스트 입문 / 옹알이 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120956

from collections import Counter
def solution(babbling):
    answer = 0
    for bb in babbling:
        cnt = Counter(replace_babbling(bb))
        check = 0
        for cc in cnt.keys():
            if cc not in ['1', '2', '3', '4']:
                check = 1
        if cnt['1'] <= 1 and cnt['2'] <= 1 and cnt['3'] <= 1 and cnt['4'] <= 1 and check == 0:
            answer += 1
    return answer

def replace_babbling(word):
    word = word.replace('aya', '1')
    word = word.replace('ye', '2')
    word = word.replace('woo', '3')
    word = word.replace('ma', '4')
    return word