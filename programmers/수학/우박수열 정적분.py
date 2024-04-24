# https://school.programmers.co.kr/learn/courses/30/lessons/134239
def solution(k, ranges):
    answer = []
    nums = hailstone(k)
    for a, b in ranges:
        b = len(nums) + b - 1
        # print(a, b)
        if a > b:
            answer.append(-1)
        elif a == b:
            answer.append(0)
        else:
            section = nums[a:b+1]
            area = 0
            for i in range(len(section) - 1):
                area += min(section[i], section[i+1])
                area += abs(section[i] - section[i+1]) / 2
            answer.append(area)
    return answer

def hailstone(num):
    nums = [num]
    while(1):
        if num % 2 == 0:
            num //= 2
            nums.append(num)
        else:
            num = 3*num + 1
            nums.append(num)
        if num == 1:
            return nums