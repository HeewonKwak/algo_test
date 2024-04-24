# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def check(arr):
    number = arr[0][0]
    sum_all = 0
    for i in arr:
        if sum(i) != number * len(arr):
            return False
    return True

def dfs(arr, answer):
    if check(arr) or len(arr) == 1:
        if arr[0][0] == 0:
            answer[0] += 1
            return
        else:
            answer[1] += 1
            return
    else:
        dfs([[arr[i][j] for j in range(0, len(arr)//2)] for i in range(0, len(arr)//2)], answer)
        dfs([[arr[i][j] for j in range(0, len(arr)//2)] for i in range(len(arr)//2, len(arr))], answer)
        dfs([[arr[i][j] for j in range(len(arr)//2, len(arr))] for i in range(0, len(arr)//2)], answer)
        dfs([[arr[i][j] for j in range(len(arr)//2, len(arr))] for i in range(len(arr)//2, len(arr))], answer)

def solution(arr):
    answer = [0, 0]
    dfs(arr, answer)
    return answer
                    
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))