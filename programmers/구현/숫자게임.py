def solution(A, B):
    answer = 0
    index = 0
    checkindex = 0
    A.sort()
    B.sort()
    for i in B:
        if A[index] < i:
            answer += 1
            index += 1
    return answer

print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))