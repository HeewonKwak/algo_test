# https://school.programmers.co.kr/learn/courses/30/lessons/43164?itm_content=course14743

# first answer
def solution(tickets):
    answer = ["ICN"]
    remain_list = []
    def dfs(start, tickets):
        if len(tickets) == 0:
            return
        lis = []
        for i in tickets:
            if i[0] == start:
                lis.append(i)

        if len(lis) == 0:
            remain_list.append(answer.pop())
            dfs(answer[-1], tickets)
        else:
            lis.sort()
            tickets.remove(lis[0])
            answer.append(lis[0][1])
            dfs(lis[0][1], tickets)
    dfs("ICN", tickets)
    if len(remain_list) > 0:
        while(len(remain_list)):
            answer.append(remain_list.pop())
    return answer

from collections import defaultdict 

def dfs(graph, N, key, footprint):
    print(footprint)

    if len(footprint) == N + 1:
        return footprint

    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = footprint[:]
        tmp.append(country)

        ret = dfs(graph, N, country, tmp)

        graph[key].insert(idx, country)

        if ret:
            return ret


def solution(tickets):
    answer = []

    graph = defaultdict(list)

    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer

# 연습
from collections import defaultdict

def dfs(graph, N, key, trip):
    if len(trip) == N + 1:
        return trip
    
    for idx, country in enumerate(graph[key]):
        graph[key].pop(idx)

        tmp = trip[:]
        tmp.append(country)
        ret = dfs(graph, N, country, tmp)
        graph[key].insert(country, idx)

        if ret:
            return ret

def solution(tickets):
    graph = defaultdict(list())
    for i, j in tickets:
        graph[i].append(j)
        graph[i].sort()

    answer = dfs(graph, len(tickets), "ICN", ["ICN"])
    return answer