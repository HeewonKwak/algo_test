# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    new_id = ch1(new_id)
    # print(new_id)
    new_id = ch2(new_id)
    # print(new_id)
    new_id = ch3(new_id)
    # print(new_id)
    new_id = ch4(new_id)
    # print(new_id)
    new_id = ch5(new_id)
    # print(new_id)
    new_id = ch6(new_id)
    # print(new_id)
    new_id = ch7(new_id)
    # print(new_id)
    # print(help(str))
    return new_id

def ch1(new_id):
    update_id = ""
    for i in new_id:
        if i.isupper():
            update_id += i.lower()
        else:
            update_id += i
    return update_id

def ch2(new_id):
    update_id = ""
    for i in new_id:
        if i.isalnum():
            update_id += i
        elif i == "_" or i == "-" or i == ".":
            update_id += i
    return update_id

def ch3(new_id):
    update_id = ""
    check = 0
    for i in new_id:
        if i == '.' and check == 1:
            continue
        elif i == '.':
            check = 1
            update_id += i
        else:
            update_id += i
            check = 0
    return update_id

def ch4(new_id):
    if len(new_id) == 0:
        return new_id
    if new_id[0] == ".":
        new_id = new_id[1:]
    if len(new_id) == 0:
        return new_id
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    return new_id

def ch5(new_id):
    if new_id == "":
        return "a"
    return new_id

def ch6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            return new_id[:-1]
        return new_id
    return new_id

def ch7(new_id):
    ll = len(new_id)
    if ll <= 2:
        a = new_id[-1]
        if ll == 1:
            return new_id + a + a
        else:
            return new_id + a
    return new_id