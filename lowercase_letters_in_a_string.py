s=str(input())
c=0
for i in s:
    if i.isalpha() and i==i.lower():
        c=c+1
print(c)