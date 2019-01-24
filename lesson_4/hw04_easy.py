# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

# Заполняем список произвольными целыми числами
print('Задание 1:')
'''
lst = []

for el in range(10):
    lst.append(random.randint(-100, 100))
print('lst = ', lst)
'''
lst=[random.randint(-10,10) for _ in range(10)]
print('lst=',lst)
kvadrat_lst=[el*el for el in lst]
print('kvadrat_lst=',kvadrat_lst)
print()

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

print('Задание 2: ')
fruit1=['груша', 'манго', 'банан', 'яблоко','апельсин']
fruit2=['лимон', 'апельсин', 'яблоко', 'грепфрут','киви']
print('fruit1=',fruit1)
print('fruit2=',fruit2)
fruit_result=[]
for fruits in fruit1:
    if fruits in fruit2:
        fruit_result.append(fruits)
print('fruit_result=',fruit_result)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
print('Задание 3: ')
lst1=[random.randint(-100,100) for _ in range(20)]
print('lst1=',lst1)
for h in lst1[:]:
    if (h%3!=0) or (h<0) or (h%4==0):
        lst1.remove(h)
print(lst1)