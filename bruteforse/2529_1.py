# 부등호
# 5 < 9 > 1 < 3 < 4
# 0 0 1 1 2 2 3 3 4  -> 숫자의 순서 따로 부등호의 순서 따로
# '0'번째 숫자와 '1'번째 숫자를 비교하는 부등호는 '0'번째 부등호

def ok(num):
    for i in range(n):      
        if a[i] == '<':     # i번째 부등호가 < 라면
            if num[i] > num[i+1]:   # i번째 숫자와 i+1번째 숫자를 비교 하는데 부등호가 다르면
                return False        # False 리턴
        elif a[i] == '>':           # 마찬가지이다.
            if num[i] < num[i+1]:
                return False
    
    return True     # if문에 한번도 걸리지 않았다면 정답이니까 True 리턴

def go(index, num):     #index는 숫자
    if index == n+1:    # n(부등호의 개수)이 2라면 3개 숫자를 쓸수 있으니까
        if ok(num):
            ans.append(num)
        return
    for i in range(10):
        if check[i]:    # i번째 숫자가 사용안되었으면
            continue    # 계속하고
        check[i] = True # True로 바꿔주면서 사용했다고 바꿔줌
        go(index+1, num+str(i))
        check[i] = False

n = int(input())
a = input().split()
ans = []
check = [False] * 10
go(0, '')
ans.sort()
print(ans[-1])
print(ans[0])