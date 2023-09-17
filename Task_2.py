from random import *
print(list := [randint(0, 100) for _ in range(int(input("Введите кол-во элементов: ")))])
min = int(input("Введите минимум: "))
max = int(input("Введите максимум: "))
result = [i for i in range(len(list)) if min < list[i] < max]
print(result)