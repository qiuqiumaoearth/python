
'''超时'''
for _ in range(int(input())):
    n,m=map(int,input().split())
    ls=list(map(int,input().split()))
    d=input()
    chu=[]
    ji=1

    for i in ls:
        ji=ji*i
    chu.append(ji%m)

    for j in d:
        if j=='L':
            a=ls.pop(0)
            chu.append(ji//a%m)
            ji=ji//a
        else:
            a=ls.pop()
            chu.append(ji //a % m)
            ji = ji // a
    #print(chu[:-1])
    for k in chu[:-1]:
        print(k,end=' ')

# for _ in range(int(input())):
#     n,m=map(int,input().split())
#     ls=list(map(int,input().split()))
#     d=input()
#     chu=[]
#     for j in d:
#         if j=='L':
#             chu.append(ls.pop(0)%m)
#         else:
#             chu.append(ls.pop()%m)
#     res=[]
#     chu.reverse()
#     cur=1
#     for k in chu:
#         cur=cur*k%m
#         res.append(cur)
#     res.reverse()
#     print(' '.join(map(str,res)))
#

    # print(' '.join(map(str,cur[::])))

# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     commands = input()
#
#     deletedNums = []
#     remainingNums = []
#
#     l = 0
#     r = n - 1
#     for i in range(len(commands)):
#         if commands[i] == 'L':
#             deletedNums.append(a[l])
#             l += 1
#         else:
#             deletedNums.append(a[r])
#             r -= 1
#     print(deletedNums)
#     t = deletedNums[-1]
#     remainingNums.append(t % m)
#     for j in range(len(deletedNums) - 2, -1, -1):
#         print(t,j)
#         t = ((t % m) * (deletedNums[j] % m)) % m
#         remainingNums.append(t % m)
#
#     for t in reversed(remainingNums):
#         print(t, end=" ")
#     print()
#


for _ in range(int(input())):
    n,m=map(int,input().split())
    ls=list(map(int,input().split()))
    d=input()
    chu=[]
    l,r=0,n-1
    for j in d:
        if j=='L':
            chu.append(ls[l]%m)
            l+=1

        else:
            chu.append(ls[r]%m)
            r-=1
    cur=1
    c=n
    for k in range(n):
        c-=1
        cur=cur*chu[c]%m
        chu[c]=cur
    print(' '.join(map(str,chu)))
