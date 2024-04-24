# 연속된 부분 수열의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/178870
def solution(sequence, k):
    answer = []
    start = 0
    end = 0
    sum_array = sequence[start]
    while end < len(sequence):
        # print(start, end, sum_array)
        if sum_array < k:
            if end == len(sequence) - 1:
                break
            sum_array += sequence[end+1]
            end += 1
        elif sum_array == k:
            if start == end:
                return [start, end]
            answer.append([start, end])
            sum_array -= sequence[start]
            start += 1
        else:
            sum_array -= sequence[start]
            start += 1
    return sorted(answer, key=lambda x: (x[1]-x[0], x[0]))[0]