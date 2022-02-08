# 부분수열의 합

n,m = map(int,input().split())          # n은 입력할 정수의 개수, m은 순열들의 목표 합
a = list(map(int,input().split()))      # n개의 정수 a[]
ans = 0                                 # 가능한 순열의 개수 ans
for i in range(1, (1<<n)):              # 일단 전체를 다 둘러본다. n자리수
    s = sum(a[k] for k in range(n) if (i & (1<<k)) > 0)     # i & (1 << k)를 이용해 k가 있는지 검사 한 후 있으면 s에 더해준다.
    if m == s:          # 구한 s 값이 m과 같으면
        ans += 1        # 개수를 나타내는 ans 1 up
print(ans)