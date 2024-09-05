# food = ['apple', 'banana', 'coconut']
# print(food[0])
# food[1] = 'peach'
# print(food)
# food.append(True) #В списке могут храниться элементы с разным типом данных!!!
# print(food)
# food.extend('string')# Перебирает значение по символам
# print(food)
# food.extend(['string', 5])
# print(food)
# food.remove('apple')
# print(food)
# print('coconut' in food)
# print('coconut' not in food)
# print(food[0:2:2])
tuple_ = 1, 2, 3, True, 'Steve'
tuple_2 = (1, 2, 3, 4)
tuple_3 = tuple([1, 2, 3, 4])
print(tuple_)
print(tuple_2)
print(tuple_3)
#tuple_[0] = 200 #Не меняется кортеж
print(tuple_)
tuple_ = 1, 2, 3, True, 'Steve'
list_ = [1, 2, 3, True, 'Steve']
print(tuple_.__sizeof__()) #размер данных
print(list_.__sizeof__())
tuple_ = ([1, 2], 3, 4) + (1, 2) #можно складывать кортежи
print(tuple_)
tuple_[0][0] = 2
print(tuple_)
tuple_ = (1, 2) * 3 # можно умножать кортежи
print(tuple_)