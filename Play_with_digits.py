n = int(input())
a = list(map(int, input().split()))
c = 0
s = 0 
for i in range(n):
    if a[i]<10:
        c = c+a[i]
    elif a[i]>9:
        while(a[i]):
            d = a[i]%10
            s = s+d
            a[i]=a[i]//10
    else:
        continue
print(s+c)