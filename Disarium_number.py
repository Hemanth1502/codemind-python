n = int(input())
a = str(n)
b = len(a)
temp = n
SOS = 0
while(n):
    d = n%10
    SOS = SOS + d**b
    n = n//10
    b-=1
if(SOS==temp):
    print(True)
else:
    print(False)