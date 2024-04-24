# https://school.programmers.co.kr/learn/courses/30/lessons/17677
def solution(str1, str2):
    answer = 0
    
    set1 = make_set(str1)
    set2 = make_set(str2)
    intersection = []
    for i in set1:
        if i in set2:
            set2.remove(i)
            intersection.append(i)
    if len(set1) == 0 and len(set2) == 0:
        return 65536
    return int(len(intersection) / ( len(set1) + len(set2)) * 65536) 

def make_set(string):
    i = 0
    str_set = []
    element = ""
    while(1):
        if not string[i].isalpha():
            if len(element) != 0:
                element = ""
        else:
            element += string[i]
        if len(element) == 2:
            str_set.append(element.lower())
            element = element[1]
        i += 1
        if i >= len(string):
            break
    return str_set