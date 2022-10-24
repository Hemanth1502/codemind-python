s=str(input())[::-1]
f=0
for i in s.split():
    k=min(i)
    if k.lower() in i:
        print(k.lower())
        break
    else:
        print(k)