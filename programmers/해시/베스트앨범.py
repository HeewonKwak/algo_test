# https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict

def solution(genres, plays):
    answer = []
    music_cnt = defaultdict(int)
    genre_sort = defaultdict(dict)
    for i in range(len(genres)):
        music_cnt[genres[i]] += plays[i]
        genre_sort[genres[i]][i] = plays[i]
    music_cnt = sorted(music_cnt.items(), key=lambda x: x[1], reverse=True)
    print(music_cnt)
    for genre, _ in music_cnt:
        scores = sorted(genre_sort[genre].items(), key=lambda x:x[1], reverse=True)
        for k in range(len(scores)):
            if k <2:
                answer.append(scores[k][0])
            else:
                break
    
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))