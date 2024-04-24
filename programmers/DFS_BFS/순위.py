# 그래프 / 순위 BFS로 풀음
# https://school.programmers.co.kr/learn/courses/30/lessons/49191#
from collections import defaultdict
def solution(n, results):
    answer = 0
    win_player, used = set(), set()
    front, back = defaultdict(set), defaultdict(set)
    for win, loss in results:
        front[loss].add(win)
        back[win].add(loss)
    for i in range(1, n+1):
        if i not in front.keys():
            win_player.add(i)
    while win_player:
        player = win_player.pop()
        used.add(player)
        for left_idx in front[player]:
            back[left_idx] = back[left_idx].union(back[player])
        for right_idx in back[player]:
            if right_idx not in used:
                win_player.add(right_idx)
            front[right_idx] = front[right_idx].union(front[player])

    for i in range(1, n+1):
        if len(front[i]) + len(back[i]) == n - 1:
            answer += 1
    return answer


# print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5,6], [6,7]]), 4)
# print(solution(6, [[1,2], [2,3], [3,4], [4,5], [5,6]]), 6)
# print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
# print(solution(6, [[1,2],[2,3],[3,4],[4,5],[5,6],[2,4],[2,6]]), 6)
# print(solution(4, [[1,2],[1,3],[3,4]]), 1)