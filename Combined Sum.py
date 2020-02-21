import math
num=input()
arr=math.factorial(len(num))
m=[]
m=list(set(num))
div=1
for i in m:
    div=div*math.factorial(num.count(i))
pos=arr//div
rep=pos//len(num)
s=0
for i in num:
    s=s+int(i)
s=s*rep
mul=1
val=0
for i in range(len(num)):
    val=val+s*mul
    mul=mul*10
if(len(m)==1):
    print("".join(num))
else:
    print(val)
************************************************************************


Given a number N, find the sum of all different arrangements of N and print that as the final answer.

Input Format

A sngle integer N

Constraints

1<=N<=10^9

Output Format

One integer denoting the sum of all possible arrangements of the number N

Sample Input 0

123
Sample Output 0

1332
Explanation 0

The Possibilities are 

123
132
213
231
312
321

Whose sum will be 1332
