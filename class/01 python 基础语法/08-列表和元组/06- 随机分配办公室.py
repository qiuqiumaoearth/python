""""
步骤：
1. 准备数据
    1.1 8位老师 -- 列表
    2.2 3个办公室 -- 列表嵌套

2. 分配老师到办公室
    *** 随机分配
    就是把老师的名字 -- 办公室列表追加老师名字数据

3. 验证是否分配成功
    打印办公室详细信息：每个办公室的人和对应老师名字
"""

import random
# 1. 准备数据
teacher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]
# 2.分配老师到办公室 --取到每个老师放到办公室列表 -- 遍历老师列表数据
for name in teacher:
    num = random.randint(0, 2)
    offices[num].append(name)
# print(offices)
i = 1
for office in offices:
    print(f'办公室{i}的人数是{len(office)}, 老师分别是:', end=' ')
    i += 1
    for a in office:
        print(a, end=' ')
    print()
