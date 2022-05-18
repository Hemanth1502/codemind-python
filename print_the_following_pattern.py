n = int(input())
temp = n
while(n):
    for i in range(temp,0,-1):
        print(i,end=' ')
    print()
    n-=1