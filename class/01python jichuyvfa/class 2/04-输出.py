a = 1.23456
print('{:.2}'.format(a))
print('%.2f' % a)
'''
%s 字符串
%d 整数
%f 浮点数
'''
# 我的年龄是xx岁

age = 18
name = 'TOM'
print('我的年龄是%d岁' % age)


xue_hao_1 = 1
xue_hao_2 = 100
print('我的学号%03d' % xue_hao_1)
print('我的学号%03d' % xue_hao_2)

# 我的姓名是xx，我的年龄是xx，我的学号是xx
print('我的姓名是%s，我的年龄是%d，我的学号是%03d' % (name, age, xue_hao_1))

# f'{表达式}' 更高效 python3.6后新增的格式化方式
print(f'我的姓名是{name}, 今年{age}岁了, 我的学号是{xue_hao_1}')

