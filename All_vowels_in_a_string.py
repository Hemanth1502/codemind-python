s=str(input())
a=[]
b=[]
for i in s:
    if i in 'aeiou':
        a.append(i)
    if i in 'AEIOU':
        b.append(i)
if len(set(a))>=5:
    print(True)
elif len(set(b))>=5:
    print(True)
else:
    print(False)