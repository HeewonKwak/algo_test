#  https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    if len(speeds) == 1:
        return [1]
    progress = 1
    day = -(-(100 - progresses.pop(0)) // speeds.pop(0))
    while(1):
        deploy = -(-(100 - progresses.pop(0)) // speeds.pop(0))
        # print(deploy, day)
        if deploy <= day:
            progress += 1
        else:
            answer.append(progress)
            progress = 1
            day = deploy
        if len(speeds) == 0:
            answer.append(progress)
            break
    return answer