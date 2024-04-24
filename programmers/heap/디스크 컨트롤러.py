from collections import deque
import heapq

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1],x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    ct, tt = 0, 0
    # while(len(q) > 0):
    #     dur, arr = heapq.heappop(q)
    #     ct = max(ct + dur, arr + dur)
    #     tt += ct - arr
    #     while len(tasks) > 0 and tasks[0][1] <= ct:


    
    return tasks

print(solution([[0, 3], [1, 9], [2, 6]]))