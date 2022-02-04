# 외판원 순회2
# 다음순열을 이용하는 이유는 경로를 그냥 1자순열로 나타낼 수 있기 때문이다.
# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2 는 다 같은 경로
# why? 다시 시작지점으로 돌아오는게 조건이기 때문에 1로 시작하는걸로 통일하면 된다.

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1
    
    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True


n = int(input())
w = [list(map(int,input().split())) for _ in range(n)]
d = list(range(n))
ans = 2147483647
while True:
    # if d[0] != 1:       # 이부분은 원래 없던 부분인데 -> 앞서 3, 4, 5라인에서 설명한 것을 수용한 부분
    #     break
    ok = True           # flag역할
    s = 0               # 경로의 합의 최소값을 저장하는 s
    for i in range(0, n-1):
        if w[d[i]][d[i+1]] == 0:    # i 지점과 i+1 지점이 거리가 0이라면
            ok = False              # 갈 수 있는 경로가 없기 때문에 Flase로 바꿔줌
            break
        else :
            s += w[d[i]][d[i+1]]    # 그게 아니라면 최소값을 나타내는 s에 더해줌
    if ok and w[d[-1]][d[0]] != 0:  # 제일 다시 0번째 지점으로 돌아오는 값을 나타냄 -1~0
        s += w[d[-1]][d[0]]
        ans = min(ans, s)
    if not next_permutation(d):     # 최소값을 구해주고 다음경로를 받아오기 위해 다음순열에 대입시켜본다.
        break

print(ans)