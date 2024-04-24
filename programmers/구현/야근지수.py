# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    answer = 0
    if sum(works) <= n:
        return answer
    work_heap = [-x for x in works]
    heapq.heapify(work_heap)
    for _ in range(n):
        max_work = -heapq.heappop(work_heap)
        max_work -= 1
        heapq.heappush(work_heap,-max_work)
    for i in work_heap:
        answer += pow(i, 2)
    return answer

# import heapq

# def solution(n, works):
#     answer = 0
#     heap = []
#     if sum(works) <= n:
#         return 0
#     for i in works:
#         heapq.heappush(heap, -i)
#     print(heap)
#     for i in range(n):
#         item = heapq.heappop(heap)
#         heapq.heappush(heap, item+1)
#     print(heap)
#     for i in heap:
#         answer += pow(i,2)
#     return answer

print(solution(4, [4,3,3]))
