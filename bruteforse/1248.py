# 맞춰봐
# 부등호 문제에서 했던거처럼 앞에서 해결하다가 중간에 안되면 더 나아가봤자 의미가없기 때문에 중간중간 확인을 해주는 것

def check(index):           # 만약 sign[1, 3]값이 + 인데 3번째 값까지 더해도 +가 아니면 '부등호'문제처럼 뒷작업을 해봤자 의미가 없기 때문에 필요한 함수
    s = 0
    for i in range(index,-1,-1):
        s += ans[i]
        if sign[i][index] == 0:
            if s != 0:
                return False
        elif sign[i][index] < 0:
            if s >= 0:
                return False
        elif sign[i][index] > 0:
            if s <= 0:
                return False
    return True

def go(index):          # 여기서 index는 A[i]의 index를 뜻한다.
    if index == n:      # index가 n과 같아지면 다한거기때문에 그만
        return True     # 
    if sign[index][index] == 0:     # sign[index][index] == 0 이면 A[index]값도 0이란 뜻이기 때문에 경우의수를 줄일수 있다.
        ans[index] = 0
        return check(index) and go(index+1)

    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if check(index) and go(index+1):
            return True
    return False

n = int(input())
s = input()
sign = [[0]*n for _ in range(n)]    # n x n 2차원 배열 0으로 초기화
ans = [0]*n                         # 0이 n개인 리스트
cnt = 0
for i in range(n):
    for j in range(i,n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1

go(0)
print(' '.join(map(str,ans)))
