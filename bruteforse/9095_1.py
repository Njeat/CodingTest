# 1, 2, 3 더하기 

T = int(input())    # test cast T
def sol(n):      
    if n == 1:
        return 1    # 숫자 1일때 1
    elif n == 2:
        return 2    # 숫자 2일때 (1+1), 2 -> 2가지
    elif n == 3:
        return 4    # 숫자 3일때 (1+1+1), (1+2), (2+1), 3 -> 4가지
    else:
        return sol(n-1) + sol(n-2) + sol(n-3)   # 그 다음 숫자들 해보니까 이런 재귀함수가 나옴

for _ in range(T):
    n = int(input())
    print(sol(n))