def xinyun(x,y):
    a = list(str(x) + str(y))
    a[0] = int(a[0])
    for i in range(1, len(a)):
        a[i] = int(a[i]) + int(a[i - 1])
    # print(a)
    if a[len(a) // 2 - 1] * 2 == a[-1]:
        return 1
    else:
        return 0

import itertools
n=int(input())
count=0

ls=list(map(int,input().split()))

for x,y in itertools.permutations(ls,2):
    if len(str(x)+str(y))%2==0:
        #print(x,y)
        count += xinyun(x, y)
print(count+n)
