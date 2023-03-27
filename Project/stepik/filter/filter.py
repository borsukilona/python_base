# фильтрация (отбор) элементов из указанного итерированного обьекта
# filter(func, *iterables) -> если func возвращает True для эелемента из *iterables, то этот элемент выводим

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(lambda x: x % 2 == 0, a)

print(next(b)) # 2
print(next(b)) # 4

c = [x for x in b] # c = list(b)
print(c) # [2, 4, 6, 8, 10]

# -------------------------------------------------------------------------------------------------------------------
# является ли число простым

def isPrime(n):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
    if count > 0:
        return False
    else:
        return True


pr = filter(isPrime, a)
print(list(pr)) # [1, 2, 3, 5, 7]

# -------------------------------------------------------------------------------------------------------------------
# выбрать названия городов, в которых присутствуют только буквенные символы

lst = ("Москва", "Рязань1", "Смоленск", "Тверь2", "Томск")

cities = filter(str.isalpha, lst)
print(list(cities)) # ['Москва', 'Смоленск', 'Томск']

# -------------------------------------------------------------------------------------------------------------------
# filter тоже итерируемый обьект, так что мы можем использовать filter внутри другого filter

numbers = a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

f1 = filter(isPrime, numbers) # отфильтровали простые числа
f2 = filter(lambda x: x % 2 != 0, f1) # из отфильтрованных простых чисел фильтурем только нечетные
# f = filter(lambda x: x % 2 != 0, filter(isPrime, numbers))

print(list(f2)) # [1, 3, 5, 7]

# -------------------------------------------------------------------------------------------------------------------
