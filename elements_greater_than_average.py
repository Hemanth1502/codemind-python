n = int(input())
a = list(map(int, input().split()))
avg = sum(a)//n
s = []
for i in range(len(a)):
    if a[i]>=avg:
        s.append(a[i])
print(len(s))