import random
# 玩家
player = int(input('请出拳：0--石头， 1--剪刀， 2--布  '))

# 电脑
computer = random.randint(0, 2)

if ((player == 0) and (computer == 1)) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print(f'玩家{player}, 电脑{computer}', '玩家获胜')
elif player == computer:
    print(f'玩家{player}, 电脑{computer}', '平局')
else:
    print(f'玩家{player}, 电脑{computer}', '电脑获胜')
