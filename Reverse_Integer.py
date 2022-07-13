n = int(input())
if n>0:
    n = str(n)[::-1]
    print(int(n))

else:
    n = str(n)
    n1 = n[0]
    n2 = n[1:]
    n2 = n2[::-1]
    n = n1 + n2
    print(int(n))