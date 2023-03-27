import random

a = random.random() # случайное число от 0 до 1
print(a) # 0.45780441678155215

b = random.uniform(1, 5)# случайное число от a до b
print(b) # 2.5047191584854147

c = random.randint(1, 5) # случайное ЦЕЛОЕ число от a до b
print(c) # 5

d = random.randrange(1, 10, 2) # случайное ЦЕЛОЕ число от a до b с шагом с (тут будет генерироваться из чисел (1, 3, 5, 7, 9))
print(d) # 7

f = random.randrange(10) # где остновиться
print(f) # 8

# ---------------------------------------------------------
# работа с последовательностями

lst = [4, 5, 0, -1, 10, 76, 3]

# выбрать один элемент из списка случайным образом
el = random.choice(lst) # получаем рандомное число из нашего списка
print(el) # 5

# перемешаем элементы в списке
shuff = random.shuffle(lst) # ничего не возвращает, а меняет исходный список
print(lst) # [0, 4, 3, 76, 5, 10, -1]

# возвратим список из неповторяющихся элементов, выбранных случайным образом
lst2 = random.sample(lst, 3) # указываем список и количество элементов, которые случайно выберет функция (элементы не будут повторяться)
print(lst2) # [3, 0, 76]

# одинаковые последовательности чисел при каждом новом запуске программы
random.seed(123) # фиксируем, чтобы получать один и тот список случайных чисел каждый раз (иначе будет разный)
lst_random = [random.randint(0,10) for i in range(20)] # список из случайных числе от 1 до 10 в диапазоне от 1 до 19 (19 элементов)
print(lst_random) # [0, 4, 1, 6, 4, 1, 0, 6, 8, 8, 5, 5, 0, 2, 2, 5, 8, 5, 3, 2]
