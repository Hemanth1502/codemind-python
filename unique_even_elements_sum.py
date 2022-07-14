n = int(input())
a = set(list(map(int, input().split())))
b = []
for i in a:
    if i%2==0:
        b.append(i)
print(sum(b))