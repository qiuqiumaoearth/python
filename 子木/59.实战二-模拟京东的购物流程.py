#创建一个空列表，用于存储入库的商品信息
lst=[]
for i in range(5):
    goods=input('请输入商品的编号和商品的名称进行商品入库，每次只能输入一件商品：')
    lst.append(goods)

#输出所有的商品信息
for item in lst:
    print(item)

#创建一个空列表，用于存储购物车中的商品
