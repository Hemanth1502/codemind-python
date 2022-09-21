t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = 0
    maxx=[a[0]]
    for z in range(1,len(a)-1):
        if a[z]>max(maxx) and a[z]>a[z+1]:
            maxx.append(a[z])
            d=d+1
    if a[0]>a[1]:
        d=d+1
    if a[-1]>max(maxx):
        d+=1
    print("Case #"+str(i+1)+':',d)