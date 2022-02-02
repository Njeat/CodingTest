# 모든순열

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
a = list(range(1,n+1))
while True:
    print(' '.join(map(str,a)))
    if not next_permutation(a):
        break       # False인 상태가 될때까지 계속 해주면서 모든 순열을 구하는 방법