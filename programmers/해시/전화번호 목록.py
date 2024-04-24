# 해시 / 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577#

def solution(phone_book):
    answer = True
    pb = set(phone_book)
    check = 0
    phone = sorted(phone_book, key=lambda x: len(x))
    for i in phone:
        for j in range(len(phone[0]), len(i)):
            if i[:j] in pb:
                return False
    return answer