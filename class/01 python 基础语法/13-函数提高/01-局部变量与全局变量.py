""" 局部变量 """
# def A():
#     a = 100
#     print(a)


# A()  # 100
# print(a)  # 报错
a = 100


def A():
    global a
    a = 200
    print(a)


A()  # 200
print(a)  # 200
# A()  # 100
# print(a)  # 报错
