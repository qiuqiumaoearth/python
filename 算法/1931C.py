t=int(input())
for zz in range(t):
	n,x,y=map(int,input().split())
	a=list(map(int,input().split()))
	ans=0
	cnt=dict()
	for i in a:
		subx=i%x
		suby=i%y
		ans+=cnt.get(((x-subx)%x,suby),0)
        #print(cnt)
		cnt[(subx,suby)]=cnt.get((subx,suby),0)+1

	print(ans)
    # print(cnt)