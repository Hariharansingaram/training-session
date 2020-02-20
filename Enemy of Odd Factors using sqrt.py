from math import sqrt as s
n=int(input())
flag=0
if (s(n)%1!=0):
    for i in range(2,n):
        if(n%i==0 and s(i)%1==0):
            flag=1
            break
else:
    flag=1
if flag==1:
    print("Friend of Odd Factor")
else:
    print("Enemy of Odd Factor")
   
   
   
 
