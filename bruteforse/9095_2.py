# 1, 2, 3 더하기 2번째 방법

def go(sum, goal):
    if(sum > goal): return 0    # sum이 n값을 넘어가면 문제오류이기 때문에 0을 리턴
    if(sum == goal): return 1   # sum이 목표값과 일치하면 1을 리턴시켜서 now의 경우의 수를 1 증가시킨다.

    now = 0     # now는 현재 경의의 수

    for i in range(1, 4): 
        now += go(sum+i, goal)  # 5번줄의 1을 계속 리턴받아 now의 경우의 수를 늘린다.
                                # sum을 1씩 증가시켜서 1을 더하는지 2를 더하는지 3을 더하는지 나타내준다.
    
    return now

T = int(input())
sum = 0
for _ in range(T):
    n = int(input())
    print(go(sum, n))