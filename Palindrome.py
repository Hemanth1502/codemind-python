n = int(input())
temp = n
r = 0
while(n):
    d = n%10
    r = r*10 + d
    n//=10
if r==temp:
    print(True)
else:
    print(False)