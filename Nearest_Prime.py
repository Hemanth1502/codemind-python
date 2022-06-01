def prime(n):
    for i in range (2,n):
        if n%i==0:
            return 0
    else:
        return 1
n = int(input())
while(n):
    N = int(input())
    for i in range(1,N+1):
        if(prime(i)):
            l=i
    i=N+1
    while(1):
        if(prime(i)):
            j=i
            break
        i+=1
    # for i in range (2,2*N):
    #     if prime(i):
    #         a.append(i)
    #     else:
    #         continue
    # g = list(set(sorted(a)))
    # d = g.index(N)
    # if abs(g[d]-g[d+1])==abs(g[d]-g[d-1]):
    #     print(min(g[d-1],g[d+1]))
    # if abs(g[d]-g[d+1])<abs(g[d]-g[d-1]):
    #     print(g[d+1])
    # if abs(g[d]-g[d+1])>abs(g[d]-g[d-1]):
        # print(g[d-1])
    if abs(l-N)==abs(j-N):
        print(min(l,j))
    elif abs(l-N)>abs(j-N):
        print(j)
    elif abs(l-N)<abs(j-N):
        print(l)
    else:
        print(N)
    n-=1