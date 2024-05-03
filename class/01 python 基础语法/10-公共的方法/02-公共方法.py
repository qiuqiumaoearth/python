str1 = 'abcdefgh'
dict1 = {'name': 'Tom', 'age': 10}
s1 = [0, 1, 2, 3]
s2 = ('a', 'b', 'c')
# enumerate ( ) 遍历对象给出下标
for i in enumerate(s2, start=1):
    print(i, end=' ')  # (0, 'a') (1, 'b') (2, 'c')


# range ( start, end, step)
# for i in range(0, 4, 2):
#     print(s1[i], end=' ')  # 0 2

# max 和 min
# print(max(s1))  # 3

# del 或者 del ( )
# del str1
# print(str1)  # NameError: name 'str1' is not defined

# len ( ) 长度
# print(len(str1))  # 8
#
# print(len(dict1))  # 2

