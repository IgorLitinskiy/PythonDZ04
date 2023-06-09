#Задача 24:
#В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
#причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.Собирающий модуль за один заход,
#находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
import os
os.system("cls")
from random import randint
print('Введите кол-во кустов: ')
B = list(randint(1, 20) for i in range(int(input())))
print(B)
a = int(input('Введите номер куста: '))
res = 0
if a == 1:
    res = B[0] + B[1] + B[-1]
if a == len(B):
    res = B[-2] + B[-1] + B[0]
else:
    res = B[a-1] + B[a-2] + B[a]
print(res, 'ягод')