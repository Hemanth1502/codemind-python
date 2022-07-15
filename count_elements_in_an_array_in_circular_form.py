n = int(input())
b = list(map(int, input().split()))
a = []
a.append(b[n-1])
a = a + b
a.append(b[0])
c = 0
for i in range(len(a)-1):
    if (a[i-1]%2!=0 and a[i+1]%2==0) or (a[i-1]%2==0 and a[i+1]%2!=0):
        c = c+1
    else:
        continue
print(c)