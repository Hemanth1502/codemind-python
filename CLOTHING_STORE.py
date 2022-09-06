n = int(input())
a = list(map(int, input().split()))
x = []
for i in a:
    if a.count(i)>=2:
        x.append(i)
y = set(x)
c1 = 0
c2 = 0
for i in y:
    if x.count(i)%2==0:
        c1 = c1+(x.count(i)//2)
    else:
        c2 = c2+(x.count(i)//2)
print(c1+c2)