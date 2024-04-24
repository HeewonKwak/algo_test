def check_word(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            cnt += 1
    if cnt == len(word1) - 1:
        return True
    else:
        return False

from collections import deque

# BFS
def solution(begin, target, words):
    if target not in words:
        return 0
    first = True
    queue = deque()
    queue.append(begin)
    check = [0 for _ in range(len(words))]
    while(len(queue)):
        word = queue.popleft()
        for i in range(len(words)):
            if check_word(words[i], word) and check[i] == 0:
                if first:
                    check[i] = 1
                    queue.append(words[i])
                    first = False
                else:
                    check[i] = check[words.index(word)] + 1
                    queue.append(words[i])
    return check[words.index(target)]

print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))