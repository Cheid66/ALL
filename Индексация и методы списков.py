food = ['apple', 'banana', 'coconut']
print(food[0])
food[1] = 'peach'
print(food)
food.append(True) #В списке могут храниться элементы с разным типом данных!!!
print(food)
food.extend('string')# Перебирает значение по символам
print(food)
food.extend(['string', 5])
print(food)
food.remove('apple')
print(food)
print('coconut' in food)
print('coconut' not in food)
print(food[0:2:2])