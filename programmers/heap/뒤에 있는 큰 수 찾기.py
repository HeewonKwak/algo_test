# 뒤에 있는 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/154539
from heapq import *
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    for i in range(n):
        value = numbers[i]
        while stack and stack[0][0] < value:
            _, idx = heappop(stack)
            answer[idx] = value
        heappush(stack, [value, i])
    return answer

# fail long time
# def solution(numbers):
#     answer = []
#     start = 0
#     end = 0
#     while(start < len(numbers)):
#         if end == len(numbers):
#             answer.append(-1)
#             start += 1
#             if start < len(numbers):
#                 if numbers[start-1] > numbers[start]:
#                     end = start + 1
#         elif numbers[start] < numbers[end]:
#             answer.append(numbers[end])
#             start += 1
#             if start < len(numbers):
#                 if numbers[start-1] > numbers[start]:
#                     end = start + 1
#             end = start + 1
#         else:
#             end += 1
#     return answer