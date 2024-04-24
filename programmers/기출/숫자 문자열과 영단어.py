# 2021 카카오 채용연계형 인턴십 / 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = ''
    if s.isdigit():
        return int(s)
    check = []
    alpa = ''
    for i in s:
        if i.isdigit():
            if alpa != '':
                check.append(alpa)
                alpa = ''
            check.append(i)
        else:
            alpa += i
    if alpa != '':
        check.append(alpa)
    ch = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for i in check:
        if i.isdigit():
            answer += i
        else:
            if i in ch.keys():
                answer += str(ch[i])
            else:
                # print(i)
                aa = ''
                for j in i:
                    # print(aa)
                    aa += j
                    if aa in ch.keys():
                        answer += str(ch[aa])
                        aa = ''
    return int(answer)