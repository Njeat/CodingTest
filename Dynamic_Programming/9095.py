# 1, 2, 3 더하기

d = [0]*11
d[0] = 1
for i in range(1, 11):
    if d[i-1] >= 0:     # 각 케이스마다 0보다 큰지 검사하는 이유는 제일 마지막 숫자를 뺀 왼쪽 부분이 -개가 되면 안되기 때문에
        d[i] += d[i-1]
    if d[i-2] >= 0:
        d[i] += d[i-2]
    if d[i-3] >= 0:
        d[i] += d[i-3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])
