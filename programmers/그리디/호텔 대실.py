# https://school.programmers.co.kr/learn/courses/30/lessons/155651#
def solution(book_time):
    answer = 0
    book_time = [[timetomin(start), timetomin(end) + 10] for start, end in book_time]
    book_time.sort()
    room = []
    for s, e in book_time:
        for i in range(len(room)):
            if room[i][1] <= s:
                room[i][0], room[i][1] = s, e
                break
        else:
            answer += 1
            room.append([s, e])
    return answer

def timetomin(time):
    h, m = map(int, time.split(':'))
    return 60 * h + m