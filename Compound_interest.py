p,r,t=map(int,input().split( ))
x = (1 + (r/100))**t
C = p*x
print("%.2f"%C)