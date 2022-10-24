s = str(input())
c=0
for i in s:
    if i.isalpha() or i.isdigit():
        continue
    elif i==' ':
        continue
    else:
        c=c+1
print(c)