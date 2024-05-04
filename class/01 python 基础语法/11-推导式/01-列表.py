#list1 = []
i = 0
# while i < 10:
#     list1.append(i)
#     i += 1
# print(list1)

# for i in range(1, 11):
#     list1.append(i)
# print(list1)

# 列表推导式
# list1 = [i for i in range(1, 10)]
# print(list1)

# list1 = [i for i in range(1, 10) if i % 2 == 0]
# print(list1)

# 多个for 循环实现推导式
# ls = [(i, j) for i in range(1, 3) for j in range(3)]
# print(ls)

ls = [(i, j) for i in range(1, 4) if i != 2 for j in range(3) if j != 0]
print(ls)
