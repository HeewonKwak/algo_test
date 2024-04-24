# 2018 KAKAO BLIND RECRUITMENT / [3차] 방금그곡
# https://school.programmers.co.kr/learn/courses/30/lessons/17683
def solution(m, musicinfos):
    answer = '(None)'
    max_music_len = 0
    m = ''.join(makesound(m))
    for musicinfo in musicinfos:
        time = timetomin(musicinfo[:11])
        name, melody = musicinfo[12:].split(',')
        melody = makesound(melody)
        mel_len = len(melody)
        if mel_len > time:
            if m in ''.join(melody[:time]) and max_music_len < time:
                answer = name
                max_music_len = time
        else:
            a, b = time//mel_len, time%mel_len
            if m in ''.join(melody) * a + ''.join(melody[:b]) and max_music_len < time:
                answer = name
                max_music_len = time  
    return answer

def timetomin(times):
    t1, t2 = times.split(',')
    h1, m1 = map(int, t1.split(':'))
    h2, m2 = map(int, t2.split(':'))
    return 60*(h2-h1) + m2 - m1

def makesound(melody):
    sound = []
    i = 0
    while 1:
        if i + 1 > len(melody):
            return sound
        elif i + 1 == len(melody):
            sound.append(melody[i])
            return sound
        if melody[i+1] == '#':
            sound.append(melody[i].lower())
            i += 2
        else:
            sound.append(melody[i])
            i += 1