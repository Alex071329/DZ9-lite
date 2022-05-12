multiple_nambers = list(input('Введите элементы списка через запятую: '))
new_set = set(multiple_nambers)
new_set.discard(',')
new_set.discard('/')
new_set.discard(';')
result = list(new_set)
print('Результат:',','.join(result))













#bad_data = 'стол;стул,диван/кравать'
#print(bad_data.replace(';', ' ').replace(',', ' ').replace('/', ' ').split())





