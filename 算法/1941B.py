for _ in range(int(input())):
    shu=int(input())
    ls=list(map(int,input().split()))
    flag=1
    a=0
    while flag and  a<shu-2:
        if ls[0]>ls[1]:
            flag=0
            break
        if ls[-1]>ls[-2]:
            flag=0
            break
        if ls[a]!=0 and a+2<=shu:
            ls[a+1]-=2*ls[a]
            ls[a+2]-=ls[a]
            ls[a]=0
        if ls[a]==0:
            a+=1
        #print(ls)
    if flag==0:
        print('NO')
    else:
        if ls.count(0)==shu:
            print('YES')
        else:
            print('NO')