# https://school.programmers.co.kr/learn/courses/30/lessons/12904
def solution(s):
    answer = 1
    for start in range(len(s)):
        for i in range(1,len(s[start:])//2 + 1):
            # if len((s[start:])) == 2:
            if s[start] == s[start+1]:
                answer = max(2, answer)
            if s[start:start+i] == s[2*i+start:i+start:-1]:
                # print(start, i)
                answer = max(2 * i + 1, answer)
            if s[start:start+i+1] == s[2*i+start + 1:start+i:-1]:
                # print(start, i)
                answer = max(2 * i + 2, answer)

    return answer