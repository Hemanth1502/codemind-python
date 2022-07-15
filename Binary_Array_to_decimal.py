n = int(input())
a = list(map(int, input().split()))
c = []
for i in range(len(a)):
    c.append((a[i])*(2**(len(a)-(i+1))))
print(sum(c))