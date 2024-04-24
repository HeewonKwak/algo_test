# 테이블 해시 함수
# https://school.programmers.co.kr/learn/courses/30/lessons/147354
def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col-1], -x[0]))
    for i in range(row_begin, row_end+1):
        hash_val = 0
        for a in data[i-1]:
            hash_val += a % i
        answer ^= hash_val
    return answer