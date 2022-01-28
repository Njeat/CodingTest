# 퇴사

n = int(input())    # 퇴사까지 남은 일수 n입력
T = [0]*(n+1)       # day를 나타내는 T배열 생성
P = [0]*(n+1)       # pay를 나타내는 P배열 생성
for i in range(1, n+1):
    T[i], P[i] = map(int, input().split())
ans = 0             # 최대수익 ans 생성
def sol(day, sum):
    global ans      # ans변수를 이 함수에서 전역변수로 사용하겠다고 선언
    if day == n+1:  # 남은 일수가 없을경우
        ans = max(ans, sum) # sum이 ans보다 더 크다면 ans에 sum저장
        return
    if day > n+1:   # 일수가 퇴사일을 넘어가면 불가능
        return
    
    sol(day+T[day], sum+P[day]) # 1일부터 차례대로 계산해서 그날 상담을 하면 day값은 늘어나고, 그에따른 수익도 늘어난다
    sol(day+1, sum) # 상담을 안하면 그날은 건너뛰기 때문에 day는 하루 늘어나고 수익은 없기때문에 sum값은 그대로


sol(1, 0)   # 1일부터 시작이고 수익은 0원으로 시작
print(ans)  
