n, k = map(int, input().split())
a = list(map(int, input().split()))
l = [[]]
c = []
count = 0
for i in range(len(a)+1):
    for j in range(i):
        l.append(a[j:i])
for i in range(len(l)):
    if len(l[i])<=1:
        if l[i]==[k]:
            count = count+1
    else:
        if sum(l[i])==k:
            count = count + 1
print(count)