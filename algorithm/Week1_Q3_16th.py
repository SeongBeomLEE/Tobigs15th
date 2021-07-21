# 주영이의 속도
def solution(m, s, dam_t, call_t):
    total_s = (m * 60) + s
    total_s = total_s - dam_t - call_t
    _m = total_s // 60
    _s = total_s % 60
    return _m, _s

m, s = map(int, input().split())
dam_t = int(input())
call_t = int(input())
m, s = solution(m, s, dam_t, call_t)
print(m, s)