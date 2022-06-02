n = int(input())
a = list(map(int, input().split()))
b = []
f = 0
for i in range (1,n+1):
    n = i*i
    b.append(n)
for j in range (len(a)):
    for k in range (len(a)):
        if a[j]==b[k]:
            f = f+a[j]
        else:
            continue
print(f)