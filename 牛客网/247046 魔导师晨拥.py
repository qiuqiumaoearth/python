# sui,hou=map(int,input().split())
# hurt=2
# xue=list(map(int,input().split()))
#
# suibiao=[i for i in range(sui)]
# boss=0
# ci=0
#
# ff=0
# xue.sort()
# for i in suibiao:
#     if xue[i]<hurt:
#         xue[i]=0
#         continue
#     if xue[i]==hurt:
#         xue[i]=0
#         hurt+=1
#     if xue[i]>hurt:
#         xue[i]-=hurt
#         suibiao.append(i)
#     if i==sui-1:
#         boss+=hurt
#         ci+=1
#         if ci==hou:
#             ff=1
#             break
# if ff==1:
#     print(boss)
# else:
#     print(boss+(hou-ci)*hurt)
#


sui,hou=map(int,input().split())
ls=list(map(int,input().split()))
hurt=2
boss=0
for i in range(hou):
    for j in range(sui):
        if ls[j]==hurt:
            hurt+=1
        if ls[j]>hurt:
            ls[j]-=hurt
    boss+=hurt
print(boss)