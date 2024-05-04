# list1 = ['name', 'age', 'gender']
# list2 = ['Tom', '20', 'man']
# dict1 = {list1[i]: list2[i] for i in range(min(len(list1), len(list2)))}
# print(dict1)
# {'name': 'Tom', 'age': '20', 'gender': 'man'}
# dict1 = {i: i**2 for i in range(1, 5)}
# print(dict1)
# # {1: 1, 2: 4, 3: 9, 4: 16}

counts = {'MBP': 268, 'HP': 125, 'Lenovo': 199, 'acer': 99}
dict1 = {key: value for key, value in counts.items() if value > 200}
print(dict1)  # {'MBP': 268}

