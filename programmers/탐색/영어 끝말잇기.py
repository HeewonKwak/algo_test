# https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    past_word = []
    past_word.append(words[0])
    end = words[0][-1]
    for i in range(1, len(words)):
        start = words[i][0]
        if start != end or words[i] in past_word:
            if (i + 1) % n == 0:
                return [n, (i + 1) // n]
            else:
                return [(i + 1) % n, (i + 1) // n + 1]
        else:
            end = words[i][-1]
            past_word.append(words[i])
        

    return [0,0]