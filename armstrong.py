n=int(input())
num=n
c=0
while num>0:
    num=num//10
    c +=1
num=n
s=0
while num>0:
    l=num%10
    num=num//10
    s+=l**c
if s==n:
    print("True")
else:
    print("False")
