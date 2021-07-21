# 등차수열을 이루는 수의 개수
def solution(x):
    cnt = 0
    for i in range(1, x + 1):
        num_li = list(map(int, str(i)))
        if i < 100:
            cnt += 1
        else:
            num_li_li = []
            for idx in range(1, len(num_li)):
                num_li_li.append(num_li[idx - 1] - num_li[idx])
            if len(set(num_li_li)) == 1:
                cnt += 1

    return cnt

x = int(input())
print(solution(x))
