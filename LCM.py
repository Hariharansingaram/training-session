n=20
l=[]
for i in range(2,n):
    while(n%i==0):
        n//=i
        l.append(i)
print(*l)
