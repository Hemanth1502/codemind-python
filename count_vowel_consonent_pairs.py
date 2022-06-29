def vowel(s):
    for i in s:
        if i in 'aeiouAEIOU':
            return 1
    else:
        return 0
def con(s):
    for i in s:
        if i in 'abcdfghjklmnpqrstvwxyzABCDFGHJKLMNPQRSTVWXYZ':
            return 1
    else:
        return 0
s = list(input())
# print(s)
k = len(s)
c = 0 
a = []
for i in range(k):
    if vowel(s[i]) and con(s[k-(i+1)]):
        a.append((s[i], s[k-(i+1)]))
    else:
        continue
print(len(a))