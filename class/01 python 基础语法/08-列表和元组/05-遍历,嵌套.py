# copy 复制列表数据
# name_list = ['TOM', 'Lily', 'Rose']
# for i in name_list:
#     print(i)

# 嵌套
name_list = [['小明', '小红', '小范'], ['TOM', 'Lily', 'Rose']]
for i in name_list:
    for j in i:
        print(j, end=' ')
    print()
