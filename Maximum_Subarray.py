n = int(input())
a = list(map(int, input().split()))
l=[]
for i in range(len(a)+1):
    for j in range(i):
        l.append(sum(a[j:i]))
print(max(l))