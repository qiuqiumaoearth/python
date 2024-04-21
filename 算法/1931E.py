for _ in range(int(input())):
    n,m=map(int,input().split())
    a=input().split()
    x=0
    b=[]
    for i in a:
        y=len(i)
        x+=y
        for j in range(y):
            if i[y-1-j]!='0':
                break
        b.append(j)
 #看每个元素后置0的个数
    b.sort(reverse=True)
    for i in range(0,n,2):#赛局可以进行的次数
        print(i)
        x-=b[i]
    if x>m:
        print('Sasha')
    else:
        print('Anna')