s = str(input())
a=[]
for i in s:
    if i in 'aeiou':
        a.append(i)
b=['a','e','i','o','u']
for i in a:
    if i in b:
        b.remove(i)
if len(set(a))>=5:
    print(0)
else:
    print(*sorted(b))