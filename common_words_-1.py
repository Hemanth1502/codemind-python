s1=(str(input()).lower()).split()
s2=(str(input()).lower()).split()
c=max(len(s1),len(s2))
count=0
for i in s1:
    if i in s2:
        count=count+1
print(count)