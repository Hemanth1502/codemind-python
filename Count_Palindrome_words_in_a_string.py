s=(str(input()).lower()).split()
c=0
for i in s:
    if i==i[::-1]:
        c=c+1
print(c)