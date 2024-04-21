# import itertools
# for _ in range(int(input())):
#     count=0
#     a=0
#     b=0
#     n,x,y=map(int,input().split())
#     s=list(map(int,input().split()))
#     for i in itertools.combinations(s,2):
#         # print(i)
#         # print(i[0])
#
#         # print(i[1])
#         a=i[0]-i[1]
#         b=i[0]+i[1]
#         if  (a%y==0 and b%x==0):
#             #print('{},{},整除{}，{}'.format(i[0],i[1],x,y))
#             count+=1
#     print(count)

# def solve():
n, x, y = map(int, input().split())
a = [int(x) for x in input().split()]
cnt = dict()
ans = 0
for e in a:
    xx, yy = e % x, e % y
    ans += cnt.get(((x - xx) % x, yy), 0)
    cnt[(xx, yy)] = cnt.get((xx, yy), 0) + 1
    print(cnt)
print(ans)

#
# for _ in range(int(input())):
#     solve()
