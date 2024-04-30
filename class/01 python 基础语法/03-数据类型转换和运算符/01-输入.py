password = input('请输入你的密码:')
print(f'你的密码是{password}')

# eval() --计算在字符串中的有效python表达式，并返回一个对象
# 就比如说原本是整数，就返回整数
str1 = '1'
print("当前类型", type(str1))
print("原本类型", type(eval(str1)))
