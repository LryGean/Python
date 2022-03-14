#
# 在____________上补充代码
#

def f(n):
    s = 0
    if n%2==1:
        for i in range(1, n+1, 2):
            s += 1/i
    else:
        for i in range(2, n+1, 2):
            s += 1/i
    return s
n = int(input())
print(f(n))