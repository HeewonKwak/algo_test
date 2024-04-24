# https://school.programmers.co.kr/learn/courses/30/lessons/49993
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        if check(skill, skill_tree):
            answer += 1
    return answer

def check(skill, skill_tree):
    tree = [i for i in skill]
    for i in skill_tree:
        if i in tree:
            if i != tree.pop(0):
                return False
    return True