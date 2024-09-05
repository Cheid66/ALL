my_dict = {'Steve':1984, 'Elvira':1987,'Nikita':2005}
print(my_dict)
print(my_dict['Elvira'])
my_dict.update({'Anna':1969,
                   'Dmitry':1965})
a = my_dict.pop('Elvira')
print(a)
print(my_dict)



my_set = {'Horse', 87, True, 'Horse', 87, 'Horse', True, ('Жиган', 'Лимон'), 'Horse', 87, 'Horse', 'Horse', True, 87, ('Жиган', 'Лимон')}
print(my_set)
list_ = (False, 'Apple')
my_set.add(list_)
my_set.discard(True)
print(my_set)
