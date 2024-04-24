mystr = ('       hello world and it '
         'and it python and nihao     ')

ss = 'hello'
print(ss.center(10, '-'))
# --hello---

print(ss.ljust(10, ','))
# hello,,,,,

print(ss.rjust(10, '/'))
# /////hello
# print(mystr.lstrip()) #删除左侧空白
# print(mystr.rstrip()) #删除右侧空白
# print(mystr.strip()) #删除所有空白
'''
hello world and it and it python and nihao     
       hello world and it and it python and nihao
hello world and it and it python and nihao

'''

# print(mystr.capitalize()) #字符串首字母大写
# # Hello world and it and it python and nihao
#
# print(mystr.title()) #每个字母首字母都大写
# # Hello World And It And It Python And Nihao
#
# print(mystr.upper())  #全部大写
# print(mystr.lower())  #全部小写

# print(mystr.replace('and', 'he', 3))

# print(mystr.split(' ', 3)) # 分割字符的

# join 合并
# mylist = ['aa', 'bb', 'cc']
# new_mylist = '...'.join(mylist)
# print(new_mylist)
# aa...bb...cc

# print(mystr.rfind('and'))
# # 23 从右边开始寻
#
# print(mystr.rindex('and'))
# # 23
# print(mystr.index('and'))
# # 12

# print(mystr.find('and'))
# # 12
#
# print(mystr.find('and', 13, 30))
# # 23
#
# print(mystr.find('ands', 13, 30))
# # -1 不存在
#
# print(mystr.index('and', 13, 30))
# # 23
#
# print(mystr.count('and'))
# # 2
#
# print(mystr.count('and', 13, 30))
# # 1

