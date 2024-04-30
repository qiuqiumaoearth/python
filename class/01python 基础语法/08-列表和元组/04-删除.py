name_list = ['TOM', 'Lily', 'Rose']

# 4. clear() -- 清空
name_list.clear()
print(name_list)  # []

# 1.del 的删除
# del name_list  # 列表被删除了
# del name_list[0]
# print(name_list)  # ['Lily', 'Rose'] 下标为0的元素被删除

# 2.pop(下标)--默认删除最后一个元素，pop(0)删除下标为0的元素
#        --返回被删除的元素
# del_name = name_list.pop(0)
# print(name_list)  # ['Lily', 'Rose']
# print(del_name)  # TOM

# 3.remove(数据)
# name_list.remove('Rose')
# print(name_list)  # ['TOM', 'Lily']

