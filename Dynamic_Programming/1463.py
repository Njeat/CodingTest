# 1로 만들기
# python은 top-down 방식이 메모리를 많이 사용하기 때문에
# bottom-up 방식만을 사용한다.

n = int(input())
d = [0]*(n+1)
d[1] = 0            # 1이면 1로만들 연산이 없기 때문에 0 -> 제일 앞에 써주어서 변수를 차단하는 것
for i in range(2, n+1):
    d[i] = d[i-1] + 1       # 1을 빼는 방법
    if i%3==0 and d[i] > d[i//3] + 1:   # 3으로 나누는 방법. 기존의 d[i]가 새로구한 d[i//3]+1 보다 크다면 최소값을 구하는 것이기 때문에
        d[i] = d[i//3] + 1              # d[i] 에 d[i//3]+1을 대입시킨다.
    if i%2==0 and d[i] > d[i//2] + 1:   # 2로 나누는 것도 마찬가지이다.
        d[i] = d[i//2] + 1

print(d[n])