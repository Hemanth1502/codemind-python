s = str(input()).lower()
s1 = s.split()
# s2 = s[0]
# a = []
# for i in s2:
#     if s2.count(i)>1:
#         a.append(i)
s3 = list(s1)
# b = []
# c = 0
# for i in range(len(s3)-1):
#     s3[i]=list(s3[i])
#     for j in a:
#         if j in s3[i]:
#             b.append(j)
#     b.append('0')
# print((s3))
# for i in b:
#     if i==' ':
#         b.remove(i)
# print(b)
b = []
for i in list(s3[0]):
    c=0
    for j in range(1,len(s3)):
        if i in s3[j]:
            c=c+1
    if c+1==len(s3):
        b.append(i)
if len(b)>0:
    print(min(b))
else:
    print(-1)