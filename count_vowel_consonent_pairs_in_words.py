def vowel(s):
    for i in s:
        if i in 'aeiouAEIOU':
            return 1
    else:
        return 0
def con(s):
    for i in s:
        if i in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            return 1
    else:
        return 0
s = str(input()).split()
# print(s)
k = len(s)
c = 0 
for i in s:
    for j in range(len(i)):
        if vowel(i[j]) and con(i[len(i)-(j+1)]):
            c=c+1
        else:
            continue
print(c)