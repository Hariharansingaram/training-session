n=int(input())
c=0
s=0
while(n):
    if(n&1):
        s=s+4**c
    c+=1
    n=n>>1
print(s)
