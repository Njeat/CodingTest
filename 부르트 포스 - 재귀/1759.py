# 암호만들기

def sol(n, alpha, password, i):
    if len(password) == n :
        if check(password):
            print(password)
        return
    if i == len(alpha):
        return

    sol(n, alpha, password+alpha[i], i+1)
    sol(n, alpha, password, i+1)

def check(password):
    ja = 0
    mo = 0

    for i in password :
        if i in 'aeiou':
            mo += 1
        else :
            ja += 1
    
    return ja >= 2 and mo >= 1

n, m = map(int, input().split())
alpha = input().split()
alpha.sort()    # 정렬되어있는 값이라고 함.
sol(n, alpha, "", 0)