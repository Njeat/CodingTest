# 1,2,3 더하기 5

limit = 100000

d = [[0]*4 for _ in range(limit+1)]
mod = 1000000009
for i in range(1, limit+1):
    if i-1 >= 0:
        d[i][1] = d[i-1][2] + d[i-1][3]    # 마지막에 +1+1이 올 수 없기 때문에 2, 3을 사용한 값
        if i == 1:
            d[i][1] = 1     # 합이 0일때
    if i-2 >= 0:
        d[i][2] = d[i-2][1] + d[i-2][3]
        if i == 2:
            d[i][2] = 1
    if i-3 >= 0:
        d[i][3] = d[i-3][1] + d[i-3][2]
        if i == 3:
            d[i][3] = 1

    d[i][1] %= mod
    d[i][2] %= mod    
    d[i][3] %= mod

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(d[n])%mod)