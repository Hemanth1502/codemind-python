s=str(input()).split()
c=0
for i in s:
    if i[0] in 'aeiouAEIOU' and i[-1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        c=c+1
print(c)