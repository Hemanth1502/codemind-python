s = str(input()).lower()
s1 = s.split()
s3 = list(s1)
b = []
for i in list(s3[0]):
    c=0
    for j in range(1,len(s3)):
        if i in s3[j]:
            c=c+1
    if c+1==len(s3):
        b.append(i)
if len(b)>0:
    print(''.join(b))
else:
    print(-1)