s = str(input())
a=[]
for i in s:
    if i in 'aeiouAEIOU':
        a.append(i)
print(len(a))