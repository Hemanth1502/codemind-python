n = int(input())
c = 0
for i in range(0, n):
    for j in range(0, n):
        for k in range(0, n):
            a = (2**i)*(3**j)*(5**k)
            if n==a:
                c = 1
                break
            else:
                continue
if c == 1:
    print('Ugly Number')
else:
    print('Not Ugly Number')