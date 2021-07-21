# 깃 충돌
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def LCM(x, y):
    ret = (x * y) // GCD(x, y)
    return ret

x, y = map(int, input().split())
print(LCM(x, y))