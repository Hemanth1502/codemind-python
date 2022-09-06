a = int(input())
b = int(input())
c = []
count = 0
for i in range(a,b+1):
    c.append(i)
lists = [[]]
for i in range(len(c) + 1):
    for j in range(i):
        lists.append(c[j: i])
for i in lists:
    if sum(i)%2!=0:
        count=count+1
print(count)