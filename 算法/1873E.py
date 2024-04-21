for _ in range(int(input())):
    n,x=map(int,input().split())
    ls=list(map(int,input().split()))
    ls.sort()
    l,r=0,10**9+x
    m=0
    def shui(a,x):
        shui1=0
        for i in ls:
            if shui1>x:
                break
            if a>=i:
                shui1+=a-i
        return shui1

    while abs(m-r)!=1:
        m= (l + r) // 2
        l1=shui(l,x)
        r1=shui(r,x)
        m1=shui(m,x)
        if x>=m1:
            l=m
        elif x<m1:
            r=m
    if r1>x:
        print(m)
    else:
        print(r)













