# 부등호
# 6 < 5 과정까지 했을때 이미 정답에서 어긋나버려서 뒤에 작업을 하는것은 의미가 없지만
# 2529_1에서는 그거까지 전부 다 계산하는 바람에 시간복잡도가 늘어나게 된다.
# 2529_2에서는 그 과정을 없애면서 시간을 줄인다.

def good(x, y, op):
    if op == '<':
        if x > y:
            return False
    if op == '>':
        if x < y:
            return False
    return True

def go(index, num):
    if index == n+1:
        ans.append(num)
        return
    for i in range(10):
        if check[i]:
            continue
        if index == 0 or good(num[index-1], str(i), a[index-1]):    # 각 자리마다 부등호가 성립할때만 숫자를 넣어주는 코드 한줄 -> 시간복잡도가 확연히 줄어든다.
            check[i] = True
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