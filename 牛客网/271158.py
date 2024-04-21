n,k=map(int,input().split())
ls=list(map(int,input().split()))
c=0
flag=0
for i in range(1,n):
    a=abs(ls[i]-ls[i-1])
    if a>k:
        if a%k!=0:
            c+=a//k
        else:
            c+=a//k-1
    if a==k:
        flag=1
if c==0 :
    if flag==0:
        print(1)
    if flag==1:
        print(0)
else:
    print(c)