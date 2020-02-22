n=5
m=n//2

for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1 or i==j and j<=m or i+j==n-1 and i<m):
            print("*",end="")
        else:
            print(" ",end="")
    print()
