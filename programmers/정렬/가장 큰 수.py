# 정렬 / 가장 큰 수
# https://school.programmers.co.kr/learn/courses/30/lessons/42746#
def solution(numbers):
    answer = ''
    nums = []
    for i in numbers:
        num = str(i)
        nums.append([num, num + (4 - len(num)) * num[0]])
    answer = ''.join([i[0] for i in sorted(nums, key = lambda x: (x[1], x[0][-1]), reverse = True)])
    if int(answer) == 0:
        return '0'
    return answer