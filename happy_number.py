n = int(input())
add = 0
while(add != 1 and add!=4):
    add = 0
    while(n):
        d = n%10
        add = add+d**2
        n = n//10
    n = add
if add==1 or add==7:
    print("True")
else:
    print("False")