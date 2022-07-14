n = int(input())
a = list(map(int, input().split()))
s = []
for i in range(len(a)):
    x = list(str(a[i]))
    for i in range(len(x)):
        x[i]=int(x[i])
    s.append(sum(x))
print(sum(s))