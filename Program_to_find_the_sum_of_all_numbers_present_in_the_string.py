n = input()
add = 0
for i in n:
    if i.isdigit():
        add = add + int(i)
print(add)