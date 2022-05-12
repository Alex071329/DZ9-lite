print('Введите количество элементов: 3')
namber = ''
while not namber.isdigit():
    namber = input('Введите 1 эленент:' )
namber = int(namber)
list_namber = []
list_namber.append(namber)
namber_2 = ''
while not namber_2.isdigit():
    namber_2 = input('Введите 2 эленент:' )
namber_2 = int(namber_2)
list_namber.append(namber_2)
namber_3 = ''
while not namber_3.isdigit():
    namber_3 = input('Введите 3 эленент:' )
namber_3 = int(namber_3)
list_namber.append(namber_3)
list_namber.sort()
print('Вывод:',list_namber)



