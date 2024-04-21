# zong=1000  #总金
# a1=0.015 #1年期定期存款利息
# a2=0.021 #2年期定期存款利息
# a3=0.0275 #3年期定期存款利息
# a5=0.03 #5年期定期存款利息
# a=0.0035 #活期存款每一季度结算一下利息

# #n为存款年数  r为年利息
# def AN(qian,n,r):
#     P=qian*(1+n*r)
#     return P

# #活期存款本息和
# def A(n,r):
#     P=1000*((1+r/4)**(4*n))
#     return P

# #一次存5年期
# print("一次存5年期 {}元".format(AN(zong,5,a5)))

# #先存两年期，到期后将本息再存三年期
# a_2=AN(zong,2,a2)
# a_2_2=AN(a_2,3,a3)
# print("先存两年期，到期后将本息再存三年期 {}元".format(a_2_2))

# #先存三年期，到期后将本息再存两年期
# a_3=AN(zong,3,a3)
# a_3_3=AN(a_2,2,a2)
# print("先存两年期，到期后将本息再存三年期 {}元".format(a_3_3))

# #先存1年，到期后将本金再存1年期，连存5次

# a=list(map(int,input().split()))
# print(max(a))

#python 前缀和  相对比直接切片，能大大减少运行时间
# n,m=map(int,input().split())
# ls=list(map(int,input().split()))  #创建一个列表来存储这些数字
# prefix=[0]*(n+2)#建立前缀和列表
# for i in range(n):
#     prefix[i+1]=prefix[i]+ls[i]
# print(prefix)  #将所有列表里面的数，都加上前面的数，求前缀和
# for i in range(m):
#     l,r=map(int,input().split())
#     print(prefix[r]-prefix[l-1])

# nums=list(map(int,input().split()))
# s=input()
# d=int(input())
# a=len(s)
# ans=0
# for i in range(a):
#     if s[i]=="R":
#         nums[i]+=d
#     if s[i]=="L":
#         nums[i]-=d
# nums.sort()
# #print(nums)
# for i in range(a):
#     for j in range(1,a):
#         if i!=j and i<j:
#             ans+=abs(nums[i]-nums[j])
# print(ans%(10**9+7))
# nums = [3,3]
# target = 6
# ans=[]
# for i in nums:
#     if target-i in nums   :
#         if nums.count(target-i)==1 and target-i==i:
#             continue
#         else:
#             print(nums.index(i),nums.index(target-i))
#             break
# for i in range(len(nums)):
#     for j in range(1,len(nums)):
#         if i!=j and nums[i]+nums[j]==target:
#             ans.append(i)
#             ans.append(j)
#             break
#
# l1 = [0]
# l2 = [0]
# if len(l1)>len(l2):
#     ls = [0] * (len(l1) - len(l2))
#     l2 += ls
# elif len(l1)< len(l2):
#     ls=[0]*(len(l2)-len(l1))
#     l1+=ls
# ans=[0]*(len(l1)+1)
# #print(l1,l2)
# for i in range(len(l1)):
#     a=l1[i]+l2[i]
#     if ans[i]+a>=10 :
#         ans[i]=(ans[i]+a)%10
#         ans[i+1]+=1
#     else:
#         ans[i]+=a
# if ans[-1]==0:
#     print(ans[:-1])
# else:
#     print(ans)
# positive_feedback = ["xrezzxgdvg","bcgx","wcfzmfosr"]
# negative_feedback = ["qyouhus","ukou","eirhfbt","qciw","for"]
# report = ["bcgx bcgx eirhfbt kvcrym bcgx cxzs eirhfbt wcfzmfosr v qciw","bcgx xrezzxgdvg bcgx xrezzxgdvg wcfzmfosr chap qyouhus biyt wcfzmfosr qciw","xrezzxgdvg wcfzmfosr ukou qcr clnj xrezzxgdvg gvtkvb qciw hi wcfzmfosr","for for mnxpqrdth bcgx bcgx qciw wcfzmfosr lspvgjvk wcfzmfosr eirhfbt","loxyg bcgx jwdesdu xrezzxgdvg wcfzmfosr rrych qyouhus wcfzmfosr klcwo xrezzxgdvg","rvbd wcfzmfosr lj xrezzxgdvg xuwguhgyyy fuz eirhfbt ukou h bcgx","bcgx wpmxyvbhc for qciw wcfzmfosr wjdm qyouhus qciw for xrezzxgdvg","bcgx sj xrezzxgdvg yjoklk bcgx hpc xrezzxgdvg lqfrvk xrezzxgdvg wcfzmfosr","qc wcfzmfosr jkjpgjalc tm v wcfzmfosr orgsqjzwa wcfzmfosr hh bfnxcx"]
# student_id = [686276715,934288178,625397331,519945877,864052244,971253305,512505036,865635090,281613863]
# k = 9
# ls=[]
# ls1=[]
# c=0
# for i in range(len(report)):
#     ans = 0
#     for j in report[i].split(" "):
#         if j in positive_feedback:
#             ans+=3
#         if j in negative_feedback:
#             ans-=1
#     ls.append((student_id[i],ans))
# ls=sorted(ls,key=lambda x:(-x[1],x[0]))
# ls1=[ls11[0] for ls11 in ls[:k]]
# print(ls1)
# #print(ls)
# #用你个蛋子的列表，煞笔煞笔煞笔
# for i in range(len(report)):
#     score = 0
#     words = report[i].split()
#     for word in words:
#         if word in positive_feedback:
#             score += 3
#         elif word in negative_feedback:
#             score -= 1
#     ls.append((student_id[i], score))
# a=list(map(int,input().split()))

# p1,p2,p3=map(int,input().split())
# ls=input()
# ls1=ls.upper()
# bu=[]
# zimu='abcdefghijklmnopqrstuvwxyz'
# shuzi='0123456789'
# weizhi=[]
# for i in range(len(ls)):
#     if ls[i]=='-':
#         if ls[i-1] in zimu and ls[i+1] in zimu and ls[i-1]!=ls[i]:
#             a=zimu.index(ls[i-1])
#             b=zimu.index(ls[i+1])
#             c=zimu[a+1:b]
#             if p3==1:
#                 for j in c:
#                     d+=j*p2
#                 bu.append((i,j))
#             else:
#                 c=c[::-1]
#                 bu.append((i,c))
#         if ls[i-1] in shuzi and ls[i+1] in shuzi and ls[i-1]!=ls[i] :
#             a = shuzi.index(ls[i - 1])
#             b = shuzi.index(ls[i + 1])
#             c = shuzi[a + 1:b]
#             if p3 == 1:
#                 bu.append((i,c))
#             else:
#                 c = c[::-1]
#                 bu.append((i,c))
#
# print(bu)

# a=[1,12,-5,-6,50,3]
# k=4
# pre=[0]*(len(a)+2)
# for i in range(len(a)):
#     if i<k:
#         pre[i+1]=pre[i]+a[i]
#     else:
#         pre[i+1]=pre[i]+a[i]-pre[i-k+1]
#
# print(max(pre)/k)

# nums = [5,14,13,8,12]
# ans=0
# if len(nums)%2==0:
#     for i in range(len(nums)//2):
#         temp=0
#         if len(nums)!=1:
#             temp=str(nums.pop(0))+str(nums.pop())
#             #print(temp)
#             ans+=int(temp)
# else:
#     for i in range(len(nums)//2+1):
#         temp=0
#         if len(nums)!=1:
#             temp=str(nums.pop(0))+str(nums.pop())
#             #print(temp)
#             ans+=int(temp)
#         else:
#             ans+=int(nums[0])
# print(ans)

# n,m=3,7
# shu=[]
# for i in range(10):
#     ls1 = [3, 3]
#     ls2 = [7, 7]
#     if n<m:
#

#B 成绩统计
# n=int(input())
# m=list(map(int,input().split()))
# zong=0
# for i in m:
#     zong+=i
# max=max(m)
# min=min(m)
# print("{:.2f} {} {}".format(zong/n,max,min))

# C简单多边形
# 找到最右边的顶点，看他的下一个顶点是否往上或者往左
# n=int(input())
# x=[]
# y=[]
# zong=[]
# ans=0
# for i in range(n):
#     a,b=map(int,input().split())
#     x.append(a)
#     y.append(b)
# d=(max(y)+min(y))/2
# for j in range(n-1):
#     if y[j]>=d:
#         if x[j]>=x[j+1] and y[j]<=y[j+1] :
#             ans+=1
# if ans!=0:
#     print('clockwise')
# else:
#     print('counterclockwise')


# a=int(input())
# b=int(input())
# c=int(input())
# shu=[]
# shu.append(a+b+c)
# shu.append(a*b*c)
# shu.append(a+(b*c))
# shu.append(a*(b+c))
# shu.append((a+b)*c)
# print(max(shu))
# ls=sorted(ls,key=lambda x:(-x[1],x[0]))

# n=int(input())
# zong=[]
# for i in range(n):
#     a,b,c=map(int,input().split())
#     zong.append((i+1,a+b+c,a))
# #print(zong)
# zong=sorted(zong,key=lambda x:(-x[1],-x[2],x[0],))
# #print(zong)
# for j in zong[:5]:
#     print(j[0],j[1])

# rains = [1,2,0,0,2,1]
# n = len(rains)
# ans = [-1] * n
# sunny = SortedList()
# rainy = {}
# for i, v in enumerate(rains):
#     if v:
#         if v in rainy:
#             idx = sunny.bisect_right(rainy[v])
#             if idx == len(sunny):
#                 print([])
#             ans[sunny[idx]] = v
#             sunny.discard(sunny[idx])
#         rainy[v] = i
#     else:
#         sunny.add(i)
#         ans[i] = 1
# print(ans)

# s = "()"
# s=list(i for i in s)
# print(s)
# x,z,d,c=0,0,0,0
# for i in s:
#     if i=='(':
#         x-=1
#     if i=='[':
#         z-=1
#     if i=='{':
#         d-=1
#     if i==')' and x==-1:
#         x+=1
#     if i==']' and z==-1:
#         z+=1
#     if i=='}' and d==-1:
#         d+=1
#     if i==')' and x==0:
#         print('flase')
#         c+=1
#         break
#     if i==']' and z==0:
#         print('flase')
#         c+=1
#         break
#     if i=='}' and d==0:
#         print('flase')
#         c+=1
#         break
# if x==z==d==c==0:
#     print('true')

# s = "()"
# dic={'(':')','{':'}','[':']','?':'?'}
# stack=['?']
# for c in s:
#     if c in  dic:
#         stack.append(c)
#     else:
#         dic[stack.pop()]!=c
#         print('flase')

#最小公倍数
# n,m=map(int,input().split())
# ans=1
# if n>m:
#     n,m=m,n
# for i in range(1,m+1):
#     if n%i==0 and m%i==0:
#         ans*=i
# print(ans)

# n,m=map(int,input().split())
# z=input()
# z=[i for i in z]
# for i in range (m):
#     a,b,c,d=map(str,input().split())
#     for j in range(int(a)-1,int(b)):
#         if z[j]==c:
#             z[j]=d
# for i in z:
#     print(i,end='')

# 关于如何判定多边形是顺时针还是逆时针对于凸多边形而言，只需对某一个点计算叉积
# = ((xi - xi-1),(yi - yi-1)) x ((xi+1 - xi),(yi+1 - yi)) = (xi - xi-1) * (yi+1 - yi) - (yi - yi-1) * (xi+1 - xi)
# 如果上式的值为正，逆时针；为负则是顺时针。
# 而对于一般的简单多边形，则需对于多边形的每一个点计算上述值，如果正值比较多，是逆时针；负值较多则为顺时针。


# import pandas as pd
# import numpy as np
# my_dataframe=pd . DataFrame (np.random.randn(4,5),index=['a','b','c','d'],columns=['e','f','j','s','k'])
# print(my_dataframe)

# n=9
# ans=0
# for i in range(1,n+1):
#     if i%3==0 or i%5==0 or i%7==0:
#         ans+=i
# print(ans)


# n = int(input())
# if n == 0:
#     break
# elif 0 < n <= 4:
#     print(n)
# else:
#     for i in range(n-4):
#         n = n + 1
#     print(n)
# def niu(n):
#     if 0 < n <= 4:
#         return n
#     return niu(n - 1) + niu(n - 4)
# while True:
#     a=int(input())
#     if a==0:
#         break
#     print(niu(a))
# while True:
#     n=int(input("验证："))
#     la=[1,2,3,4]
#     if n<=4:
#         print(la[n-1])
# #     else:
# ls=[0,1,2,3]
# while True:
#    a = int(input())
#    if a>4:
#        for i in range(4,a+1):
#            b=ls[i-1]+ls[i-3]
#            n.append(b)
#        print(n[a])
#    elif a==0:
#        break
#    else:
#        print(a)

# from itertools import combinations
# nums = [1,2,4,5,10]
# ans=0
# dict={}
# for  i in combinations(nums,2):
#     #print(i)
#     a=i[0]*i[1]
#     if a in dict:
#         dict[a]+=1
#     else:
#         dict[a]=1
#
# result=0
# for j in dict.values():
#     result+=j*(j-1)//2
# print(result*8)

# from collections import Counter
# arr = [5,5,4]
# k = 1
# a=set(arr)
# ls=[]
# ans=0
# ls=Counter(arr).values()
# print(ls)
# for j in ls:
#     #print(j)
#     k -= j
#     if k<0:
#         ans+=1
# print(ans)

# length = 1000
# width = 35
# height = 700
# mass = 300
# B=0
# H=0
# if length >=10000 or width>=10000 or height>=10000 or mass>=10000 or length*width*height>=10**9:
#     B+=1
# if mass>=100:
#     H+=1
# if B==H==1:
#     print("Both")
# if B==H==0:
#     print("Neither")
# if B==1 and H==0:
#     print("Bulky")
# if B==0 and H==1:
#     print("Heavy")

#三角形的面积
# a,b,c=map(int,input().split())
# p=(a+b+c)/2
# s=(p*(p-a)*(p-b)*(p-c))**(1/2)
# print("{:.1f}".format(s))

#DFS 深度优先搜索
# n=3
# edges = [[0,1],[0,2],[1,2]]
# la=[]
# for i in range(n):
#
# from Crypto.Util.number import *
# c=b'ipfm\x82Kj]p~l?\x82ogw\x85mt[K\x8br\x97'
# a=3
# flag=''
# for i in c:
#     flag+=chr(i-a)
#     a+=1
# print(flag)
#
# tmp='\xbe\xfc\xca\xc2'
# print tmp.decode('gbk').encode('utf-8')
#
# s = b'ipfm\x82Kj]p~l?\x82ogw\x85mt[K\x8br\x97'
# ss = s.decode()
# print(type(ss))
# print(ss)

# s = b'\xe7\xbb\x9d\xe5\x9c\xb0\xe6\xb1\x82\xe7\x94\x9f'
# ss = s.decode()
# print(type(ss))
# print(ss)
#
# pythonCopy codeimport chardet
# data = b'\xbc\xde\xcf\xbc'
# result = chardet.detect(data)
# encoding = result['encoding']
# decoded_data = data.decode(encoding)

# from crypto.Util.number import *
# c=b'ipfm\x82Kj]p~l?\x82ogw\x85mt[K\x8br\x97'
# a=3
# flag=''
# for i in c:
#     flag+=chr(i-a)
#     a+=1
# print(flag)

# a,b,c=map(int,input().split())
# a1=0
# for i in range(1,a+1):
#     a1+=i
#
# b1=0
# for j in range(1,b+1):
#     b1+=j**2
#
# c1=0
# for k in range(1,c+1):
#     c1+=1/k
#
# sum=a1+b1+c1
#
# print("{:.2f}".format(sum))

# N=int(input())
# for i in range(2,N+1):
#     for j in range(2,i**(1/2)+1):
#

# N=int(input())
# for i in range(2,N+1):
#    julge=1
#    for j in range(2,int(i**0.5)+1):
#        if i%j==0:
#            julge=0
#            break
#    if julge==1:
#        print(i)
#        list1.append(i)
# for i in list1:
#    print(i)

# ls=list(input())
# ls=sorted(ls)
# ls_set=set(ls)
# ans=[]
# for i in ls_set:
#     ans.append([i,ls.count(i)])
# ans=sorted(ans,key=lambda x:(-x[1],x[0]))
# print(ans[0][0])
# print(ans[0][1])

# ls=[0,1,1,2,3]
# a=int(input())
# for i in range(4,a+1):
#     ls.append(ls[i-1]+ls[i])
# #print(ls)
# print(ls[a-1]*ls[a+1]-ls[a]**2)

# import itertools
# n=int(input())
# ls=list(map(int,input().split()))
# for i in itertools.combinations(ls,3):
#     if i[0]+i[1]>i[2] and i[0]+i[2]>i[1] and i[1]+i[2]>i[0]:
#         for j in i:
#             print(j,end=' ')
#         break
# else:
#     print("No solution")

# n,x=map(int,input().split())
# #print(ans)
# ans=0
# for i in range(1,n+1):
#     ans+=str(i).count(str(x))
# print(ans)
#
# n=list(input())
# b=tuple(n)
# a=list(b)
# n.reverse()
# #print(a,n)
# for i in n[1:]:
#     a.append(i)
# str="".join(a)
# str=int(str)
# p=1
# for j in range(2,int(str**(0.5)+1)):
#     if str%j==0:
#         p=0
#         break
# if p==1:
#     print('prime')
# else:
#     print('noprime')

# ling=[1,2,3,5,7]
# yi=[4,6,9,0]
# er=[8]
# n=int(input())
# ans=0
# for i in range(n):
#     a,b=map(int,input().split())
#     if a==b:
#         if a in ling:
#             ans=0
#         if a in yi:
#             ans=1
#         if a in er:
#             ans=2
#     else:
#         for j in range(a,b+1):
#             #print(j)
#             for k in str(j):
#                 print(k)
#                 if k in ling:
#                     ans+=0
#                 if k in yi:
#                     ans+=1
#                 if k in er:
#                     ans+=2
#             print(ans)

# ls=[1,0,0,0,1,0,1,0,2,1,1]
# n=int(input())
#
# for i in range(n):
#     a,b=map(int,input().split())

# n=int(input())
# for i in range(n):
#     a,b=map(int,input().split())
#     c=a**(0.5)
#     d=b**(0.5)
#     if c* c == a:
#         print(d - c + 1)
#     else:
#         print(d - c)

# book,reader=map(int,input().split())
# book_ls=[]
# for i in range(book):
#     book_ls.append(int(input()))
# book_ls.sort()
# qv=[]
# print(book_ls)
# #book_ls=[23, 24, 24,  2123]
# reader=5
# for j in range(reader):
#     len,req=map(str,input().split())
#     for k in book_ls:
#         if str(req) in str(k):
#             print(k)
#             book_ls.remove(k)
#             break
#     else:
#         print("-1")

#字符串是否在字符串中
# a="123"
# b=input()
# if str(a) in str(b):
#     print(1)
# else:
#     print(0)

# a=123
# b=[1456,1234,2134,3123]
# for i in b:
#     if str(a) in str(i):
#         print(a,i,"ok")
#     else:
#         print("no")
#         qv.append(a)
#     else:
#         qv.append("-1")
# print(qv)

# import math
# s,v=map(int,input().split())
# t=math.ceil(s/v)+10
# a=8*60-t
# if a>=0:
#     b=a//60
#     c=a%60
#     print('0'+"{}:{}".format(b,c))
# else:
#     a=24*60+a
#     b = a // 60
#     c = a % 60
#     if len(str(a))==2:
#         print("{}:{}".format(b, c))
#     else:
#         print('0' + "{}:{}".format(b, c))

# sum=0
# n=input()
# for i in n:
#     #print(i)
#     sum+=int(i)
#     print(sum)
# list1 = [0] * 200001
# sum2 = 0
# for i in range(1,200001):
#     p = i
#     sum1 = 0
#     while p:
#         sum1 += p%10
#         p //= 10
#     sum2 += sum1
#     list1[i] = sum2
# s=int(input())
# for i in range(s):
#     n = int(input())
#     print(list1[n])
# for _ in range(s):
#     n=int(input())
#     sum=0
#     for i in range(1,n+1):
#         for j in str(i):
#             #print(j)
#             sum+=int(j)
#     print(sum)

# ls=[0]*200001
# sum2=0
#
# for i in range(1,200001):
#     p=i
#     sum1=0
#
#     while p:
#         sum1+=p%10
#         p//=10
#     sum2+=sum1
#     ls[i]=sum2
#
# n=int(input())
# for j in range(n):
#     m=int(input())
#     print(ls[m])

# import bisect
# ls=[1,4,5,9,10]
# index1=bisect.bisect(ls,6)
# index2=bisect.bisect_right(ls,6)
# index3=bisect.bisect_left(ls,6)
# print('index1={},index2={},index3={}'.format(index1,index2,index3))

# shu,changdu=map(int,input().split())
# ls=list(map(int,input().split()))
# ls.sort()
# left,right,mid=0,0,0
# right=ls[0]-0
# left=changdu-ls[-1]
# for i in range(1,shu):
#     temp=ls[i]-ls[i-1]
#     if mid<temp:
#         mid=temp
# print('{:.10f}'.format(max(left,right,mid/2)))

'''22'''
# ci=int(input())
# for _ in range(ci):
#     shu,num=map(int,input().split())
#     ls=list(map(int,input().split()))
#     if shu == 1:
#         tt=str(ls[0])
#         a1 = tt.lstrip('0')
#         a2 = tt.rstrip('0')
#         a=min(a1,a2)
#         if int(a) > 10 ** num:
#             print(shu,num,ls,'Sasha')
#         else:
#             print(shu,num,ls,'Anna')
#     else:
#         zero=0
#         zong=0
#         for i in ls:
#             temp=0
#             temp1=0
#             p=str(i)
#             temp=p.count('0')
#             temp1=len(p)
#             zero+=temp
#             zong+=temp1
#         if zong-min(zero,shu-1)>=num:
#             print(shu,num,ls,'Sasha')
#         else:
#             print(shu,num,ls,'Anna')






# for i in range(6):
#     print(6-i)


# a='1010'
# a1=a.lstrip('0')
# a2=a.rstrip('0')
# print(a1,a2)









