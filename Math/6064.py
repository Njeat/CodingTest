#카잉 달력


t = int(input())
for _ in range(t):
    m,n,x,y = map(int,input().split())
    x -= 1  #1을 빼줘서 나머지값을 구하는거야
    y -= 1  #마찬가지
    k = x   #k가 원하는 년도야
    while k < n*m:
        if k%n == y:    #x값은 맞춰놨으니까 y값만 계산하면 돼
            print(k+1)  #정답이 맞으면 1씩 뺐으니까 다시 1 더해줘서 출력
            break
        k += m  #m으로 나눈 나머지가 x인 모든 k에 대해서 조사할 수 있다.
    else:
        print(-1)