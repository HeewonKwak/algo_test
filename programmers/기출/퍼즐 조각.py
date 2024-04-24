def solution(input_list):
    answer = 0
    cnt = [2, 1]
    if input_list[0] == 1:
        cnt[0] += 1
    for i in range(1, len(input_list)):
        if input_list[i] == 1:
            cnt[0], cnt[1] = sum(cnt) * 3 - cnt[1], sum(cnt) * 1
        else:
            cnt[0], cnt[1] = sum(cnt) * 2 - cnt[1], sum(cnt) * 1
    return sum(cnt)

aa = [1, 0, 1, 1]
print(solution(aa))