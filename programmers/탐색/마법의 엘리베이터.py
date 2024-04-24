# https://school.programmers.co.kr/learn/courses/30/lessons/148653#
def solution(storey):
    answer = 0
    num = list(map(int, list(str(storey)[::-1])))
    idx = 0
    num.append(0)
    # print(num)
    while idx < len(num):
        # print(idx, answer, num)
        if idx == 0 and num[idx] == 5 and num[idx+1] >= 5:
            answer += 10 - num[idx]
            ii = idx
            while 1:
                num[ii+1] += 1
                if num[ii+1] != 10:
                    break
                num[ii+1] = 0
                ii += 1
        elif num[idx] < 6:
            answer += num[idx]
        else:
            answer += 10 - num[idx]
            ii = idx
            while 1:
                num[ii+1] += 1
                if num[ii+1] != 10:
                    break
                num[ii+1] = 0
                ii += 1
        idx += 1
    return answer