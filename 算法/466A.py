n,m,a,b=map(int,input().split())
danjia=b/m
qian=0
qian_1=0

if danjia<=a:
    qian_1=n//m*b
    qian=min(qian_1+b,qian_1+n%m*a)
else:
    qian=n*a
print(qian)