# s1 = str(input()).lower()
# s2 = str(input()).lower()
# # print(s1)
# # print(s2)
# a = []
# for i in s2:
#     if i not in s1:
#         a.append(i)
#     else:
#         continue
# for i in s1:
#     if i not in s2:
#         a.append(i)
#     else:
#         continue
# b = []
# for i in a:
#     if i not in b:
s1 = list(str(input().lower()))
s2 = list(str(input().lower()))
s1 = list(set(s1))
s2 = list(set(s2))
a = []
for i in s1:
    if ' ' in s1:
        s1.remove(' ')
    else:
        continue
for i in s2:
    if ' ' in s2:
        s2.remove(' ')
    else:
        continue
for i in s1:
    if i not in s2:
        a.append(i)
    else:
        continue
for i in s2:
    if i not in s1:
        a.append(i)
    else:
        continue
a = ''.join(sorted(a))
print(a)
# print(s1, s2)
#         b.append(i)
#     else:
#         continue
# print(''.join(sorted(b)))
