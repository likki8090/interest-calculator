"""a=input()
b=input()
a=a.upper()
b=b.upper()
a1=[0]*26
b1=[0]*26
for i in a:
    if(ord(i)>=97 and ord(i)<=122):
        a1[ord(i)-97]+=1
for i in b:
    if(ord(i)>=97 and ord(i)<=122):
        b1[ord(i)-97]+=1

if a1==b1:
    print("Yes")
else:
    print("no")
====================================================================
"""
'''n=int(input())
a=[3,2,1,7,5,4]
max=0
min=999999
even=[]
odd=[]
"""for i in range(0,n):"""

for i in range(0,n):
    if(i%2==0):
        if a[i]<min:
            min=a[i]
            odd.appen(min)
    else:
        if a[i]>max:
            max=a[i]
            even.append(max)

print(min,max,end=" ")
============================================================'''

'''n=int(input())
m=int(input())
sum1=0
sum2=0
for i in range(1,m+1):
    if(i%n==0):
        sum1=sum1+i
    else:
        sum2=sum2+i
print(abs(sum1-sum2))
========================================================'''
'''n=int(input())
sum=0
if(n!=0):
    while(n>0):
        r=n%10
        sum=sum+r
        n=n//10
    if(sum%9==0):
        print(9)
    else:
        print(sum%9)
else:
    print(0)

n=int(input())
if n==0:
    print(0)
elif n%9==0:
    print(9)
else:
    print(n%9)
================================================================='''
'''n=int(input())
for row in range(n, 1-1, -1):
    for col in range(1,row+1):   
        print(col,end=" ")   for 2nd output change col==>row
        
    print()
    1  2  3  4  5      1  1  1  1
    1  2  3  4         2  2  2
    1  2  3            3  3  
    1  2               4
    1
========================================================================'''
'''n=int(input())
for row in range(1,n+1):
    for col in range(n,0,-1):               1           1
        if row >= col:                     2 2         2 1
            print(row,end=" ")            3 3 3       3 2 1
        else:                            4 4 4 4     4 3 2 1
            print("",end=" ")  
    print()
    row==>col for 2nd o/p
========================================================================='''
'''
n=int(input())
for row in range(n,0,-1):
    for col in range(1,n+1):                   5
        if row <= col:                        4 5
            print(col,end=" ")               3 4 5
        else:                               2 3 4 5
            print("",end=" ")              1 2 3 4 5
    print()
============================================================================'''

'''def fun(a,b):
    if((4-a)<(a-b) and 3<b):
        a=2+1+a
        a=2+1+a
        b=3+a+b
        return fun(a,b+1)
    
    return b-a+1
    
a=int(input())
b=int(input())
print(fun(a,b))
=====================================================================================
p=7
q=4
r=8
for r in range(3,6):
    if((q+r)>(r-q) or q<r):
        q=(r+p)+r
        p=(r+p)+r
    
    q=4+p
    if((6+p)<q):
        q = r+p
        break

print (p+q+r)
=========================================================================='''




