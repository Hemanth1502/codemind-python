s = list((str(input()).lower()))
for i in s:
    if ' ' in s:
        s.remove(' ')
print(''.join(sorted(set(s))))