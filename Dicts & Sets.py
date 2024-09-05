phone_book = {'Steve':89506558558, 'Elvira':89527259601} #ключ + значение через ":" = 1 объект
print(phone_book)
print(phone_book['Steve'])
phone_book['Steve'] = 123456789
phone_book['Anton'] = 159753258 #Добавление элемента словаря
#del phone_book['Elvira'] #Удаление элемента словаря
phone_book.update({'Max':123654799,
                  'Diana':88005555555,
                   'Arseniy':88004567891})# Внесение нескольких значений в словарь
#В словаре элементы не уорядочены
# print(phone_book.get('Misha', 'Такого значения нет'))
# print(phone_book)
# a = phone_book.pop('Elvira')
# list_ = [1, 2, 3]
# list_.pop(0)
# print(list_)
# print(phone_book)
# print(a)
print(phone_book.keys()) #Ключи словаря
print(phone_book.values()) #Значения ключей словаря
print(phone_book.items()) #Ключи со значениями
set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'Elvira', False, (1, 2, 3)} #Множества - хранение уникальных значений
print(set_)
list_ = [1, 1, 1, 3, 3, 1, 2, 2, 7, 2, 1, 5]
list_ = set(list_)
print(list_)
print(list_.discard(1)) #То же - Remove, но не выдаст ошибку, если обращение к несуществующему элементу
print(list_)
print(list_.add(9))
print(list_)