#question
Given a number N, Find the number of 1's in the binary equivalent of the number.
Input Format
One integer N
Constraints
N
Output Format
One integer value denoting the number of 1's
Sample Input 0
5
Sample Output 0
2
Explanation 0
Binary of 5 is 101, which has 2 ones in it
#answer
a=int(input())
b=bin(a)
d=str(b)
print(d.count("1"))
