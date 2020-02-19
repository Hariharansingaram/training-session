n=int(input())
b=str(n)
if(b[0]=='-'):
    m='-'+str(int(b[1:][::-1]))
else:
    m=int(b[::-1])
print(m)
