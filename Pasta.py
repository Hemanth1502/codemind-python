n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = []
c = 0
for i in b:
    if i not in d:
        d.append(i)
    else:
        continue
for i in d:
    if i in a:
        c = c+1
    else:
        continue
# print(a)
# print(d)
if len(b)==c:
    print('Yes')
else:
    print('No')