# 스타트와 링크

def go(index, first, second):
    if index == n:
        if len(first) != n//2:
            return -1
        if len(second) != n//2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]     # t1은 first팀의 능력치를 더한것
                t2 += s[second[i]][second[j]]   # t2는 second팀의 능력치를 더한것
        diff = abs(t1-t2)   # 두 팀의 능력치 차이를 빼고
        return diff         # 그 결과값을 리턴
    if len(first) > n//2:   # 한팀에 n의 반 인원보다 많이 들어갈 경우
        return -1           # 함수 빠져나오기
    if len(second) > n//2:  # first와 마찬가지
        return -1
    ans = -1
    t1 = go(index+1, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1):    # 능력치 차이의 최소값을 구하는거
        ans = t1                                # 
    t2 = go(index+1, first, second+[index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)] # python의 2차원배열 받는문법
print(go(0,[],[]))