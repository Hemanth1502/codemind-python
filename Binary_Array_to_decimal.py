n = int(input())
a = list(map(int, input().split()))
k = len(a)-1
c = 0
for i in range(len(a)):
    if a[i]==1:
        c = c + (a[i]*2)**(k) #8 + 4 + 
        k = k-1
    else:
        k = k-1
print(c)