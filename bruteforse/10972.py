# 다음순열
# 7 2 3 6 5 4 1

def next_permutation(a):
    i = len(a)-1        # i를 수열의 마지막 인덱스로 지정
    while i > 0 and a[i-1] >= a[i]: # i가 첫번째 인덱스는 아니고 i-1번째 숫자가 i숫자보다 작아야돼
        i -= 1          # i를 계속 감소시켜서 i-1일때 더 큰수가 나오는지 확인하려고
    if i <= 0:          # i가 0보다 작아지면 다음순열은 없다는 얘기 -> 이미 마지막 순열이라는 얘기
        return False    # 따라서 False리턴
    j = len(a)-1        # j는 i-1보다는 크지만 그 뒤숫자들 중에 제일 작은수 7 2 3 6 5 4 1 에서 3이 i-1 이고 4가 j를 뜻한다.
    while a[j] <= a[i-1]:   # j번째 숫자가 4니까 len(a)-1번째 숫자인 1에서 한칸 내려온거지 a[i-1]이 3이니까 작을때까지
        j -= 1              # j를 - 해준다.

    a[i-1],a[j] = a[j],a[i-1]       # a[j]가 4인걸 찾았으니가 a[i-1]인 3이랑 swap해주기 -> 7 2 4 6 5 3 1

    j = len(a)-1        # 다시 j를 제일 마지막 인덱스로 놔주고
    while i < j:        # 현재 i인 3, j인 6이 교차될때까지
        a[i],a[j] = a[j],a[i]   # 뒤의 숫자인 6 5 3 1에서 6과 1을 바꿔주면 1 5 3 6
        i += 1                  # i는 증가시켰으니까 4 
        j -= 1                  # j는 감소시켰으니까 5  하고 다시 18번라인 가서 5 3 을 바꿔주면 1 3 5 6 다시 19,20을 하면 17번라인에서 걸리니까 while문을 나옴

    return True                 # 따라서 7 2 4 1 3 5 6이 된다.

n = int(input())
a = list(map(int,input().split()))
if next_permutation(a):
    print(' '.join(map(str,a)))
else:
    print(-1)