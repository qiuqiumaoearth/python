# 只要有对应键
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}

# 5. items ( ) -- 返回可迭代对象 -- 所有键值对
# print(dict1.items())  # dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])
# for i in dict1.items():
#     print(i)
# ('name', 'Tom')
# ('age', 20)
# ('gender', '男')

# 4.values ( ) -- 返回可迭代 -- 值
# print(dict1.values())
# for i in dict1.values():
#     print(i, end=' ')

# 3. keys ( ) -- 返回一个可迭代数据 -- 键
# print(dict1.keys())  # dict_keys(['name', 'age', 'gender'])
# for i in dict1.keys():
#     print(i, end=' ')  # name age gender

# 2. get ( )
# print(dict1.get('age'))  # 20
# print(dict1.get('id', 100))  # 100
# print(dict1.get('id'))  # None

# 1. [key]
# print(dict1['name'])  # Tom

# 3. 修改
# dict1['name'] = 'Lily'
# print(dict1)  # {'name': 'Lily', 'age': 20, 'gender': '男'}


# 2. 删除
# del dict1['name']
# print(dict1)  # {'age': 20, 'gender': '男'}
# del(dict1)
# print(dict1)  # NameError: name 'dict1' is not defined
# 空字典
# dict2 = {}

# 1. 增加
# 如果key 存在则修改这个key对应的值，否则增加key值
# dict1['name'] = 'Rose'
# print(dict1)  # {'name': 'Rose', 'age': 20, 'gender': '男'}
# dict1['id'] = '11'
# print(dict1)  # {'name': 'Rose', 'age': 20, 'gender': '男', 'id': '11'}
