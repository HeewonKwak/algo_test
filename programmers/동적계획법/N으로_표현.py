# 동적 계획법
# https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3

def cal(nums1, nums2):
    final = set()
    for i in nums1:
        for j in nums2:
            final.add(i+j)
            final.add(i-j)
            final.add(i*j)
            if j != 0:
                final.add(i//j)
    return final

def solution(N, number):
    nums = dict()
    nums[1] = set([N])
    if N == number:
        return 1
    for i in range(2, 9):
        temp_list = set([int(str(N)*i)])
        for j in range(1, i):
            temp_list.update(cal(nums[i-j], nums[j]))
        # print(temp_list)
        if number in temp_list or -number in temp_list:
            print(temp_list)
            return i
        nums[i] = temp_list
        # print(nums)
        
    return -1


print(solution(5, 12))

# 복습
def solution(N, number):
    dp = [set()] * 9
    for i in range(1, 9):
        dp[i] = set([N * int('1'*i), -N * int('1'*i)])
        for j in range(1,i):
            dp[i] = dp[i].union(calculator(dp[j], dp[i-j]))
        if number in dp[i]:
            return i
    return -1

def calculator(dp1, dp2):
    new = set()
    for a in dp1:
        for b in dp2:
            new.add(a+b)
            new.add(a-b)
            new.add(a*b)
            if b != 0:
                new.add(a//b)
    return new