n = int(input())
a = str(n)
c = len(a)
add = 0
temp = n
while(n):
    d = n%10
    add = add+d**c
    n = n//10
    c-=1
if(temp == add):
    print(True)
else:
    print(False)