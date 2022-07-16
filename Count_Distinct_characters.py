s = list(str(input()).lower())
for i in s:
    if i==' ':
        s.remove(i)
print(len(sorted(set(s))))