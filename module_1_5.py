immutable_var = tuple(['H2O', 15, True])
print(immutable_var)
#immutable_var[1] = 51
#print(immutable_var)
#объекты кортежа невозможно изменить, если они не являются списком (можно менять элементы списка внутри кортежа)

mutable_list = ['Tree', 'Bird', True, 20]
print(mutable_list)
mutable_list[-1] = False
print(mutable_list)