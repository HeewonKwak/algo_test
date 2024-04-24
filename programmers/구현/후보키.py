# https://school.programmers.co.kr/learn/courses/30/lessons/42890
from collections import defaultdict
from itertools import combinations

def solution(relation):
    answer = []
    cc = defaultdict(list)
    for i in relation:
        for j in range(len(i)):
            cc[j].append(i[j])
    check = []
    for i in range(len(cc)):
        if len(set(cc[i])) == len(relation):
            answer.append(i)
        else:
            check.append(i)
    if len(relation) == 1:
        return len(answer)
    ii = 2
    while(1):
        if ii > len(relation):
            break
        for i in combinations(check, ii):
            xxx = []
            for y in range(len(relation)):
                aaa = []
                for x in i:
                    aaa.append(cc[x][y])
                if aaa not in xxx:
                    xxx.append(aaa)
                else:
                    break
            else:
                for aa in answer:
                    if type(aa) == int:
                        bb = {aa}
                    else:
                        bb = set(aa)
                    if set(i).union(bb) == set(i):
                        break
                else:
                    answer.append(i)
        ii += 1
    return len(answer)