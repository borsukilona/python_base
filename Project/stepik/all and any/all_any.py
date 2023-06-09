a = [True, True, True, True]
b = all(a)
print(b) # True (потому что все элементы равны между собой)

с = [True, False, True, True]
b = all(с)
print(b) # False (потому что все элементы не равны между собой)

# ---------------------------------------------------------------

d = [0, 1, 2.5, "", "python", [], [1, 2], {}]
b = all(d)
print(b) # False

'''
все элементы списка приводятся к булевому значению: пустота (0,[],{},"") = False, непустота (1,[1,2],"bla") = True)
таким образом наш список d = [False, True, True, False, True, False, True, False]
'''

d1 = [1, 2.5, "python", [1], [1, 2]]
b = all(d1)
print(b) # True (все элементы НЕ пустые)

# ---------------------------------------------------------------
# функцию all можно изобразить вот так:

all_res = True
for x in d:
    all_res = all_res and bool(x)

# функцию any можно изобразить вот так:

any_res = False
for x in d:
    any_res = any_res or bool(x)

# ---------------------------------------------------------------
# any похожа на all, только возвращает True, если встретилось ХОТЯБЫ ОДНО значение

d = [0, 1, 2.5, "", "python", [], [1, 2], {}]
b = any(d) # True (хотябы один эелемнт не пустой)

print(any([0, [], {}, ""])) # False (все элементы пустые)

# ---------------------------------------------------------------
# у нас есть крестики-нолики, и мы хотим определить, есть ли выигрышная позиция у крестиков


def true_x(x):
    return x == 'x'


P = ['x', 'x', 'o', 'o', 'x', 'o', 'x', 'x', 'x']
'''
x x o
o x o
x x x
'''

# есть ли три крестика подряд в строке (каждая строка = 3 элемента)
'''
row_1 = all(map(lambda x: x == 'x', P[:3])) # первая строка (первые 3 элемента)
row_2 = all(map(lambda x: x == 'x', P[3:6])) # вторая строка
row_3 = all(map(lambda x: x == 'x', P[6:])) # третья строка
'''

row_1 = all(map(true_x, P[:3]))
row_2 = all(map(true_x, P[3:6]))
row_3 = all(map(true_x, P[6:]))

print(row_1, row_2, row_3)
# False False True

# есть ли три крестика подряд в столбце (каждый столбец = 3 элемента)

col_1 = all(map(true_x, P[::3]))
col_2 = all(map(true_x, P[1::3]))
col_3 = all(map(true_x, P[2::3]))

print(col_1, col_2,col_3)
# False True False

# есть ли три крестика подряд в диагонали (каждый столбец = 3 элемента)

diag_1 = all(map(true_x, P[0::4]))
diag_2 = all(map(true_x, P[2::2]))
print(diag_1, diag_2)
# True False

if any([diag_1, diag_2]) or any([col_1, col_2, col_3]) or any([row_1, row_2, row_3]):
    print("yes")
else:
    print("no")
# yes

# ---------------------------------------------------------------
# делаем игру сапер

# ировое поле 10х10 элементов
N = 10
Pole = [0] * (N*N)

# тут будет мина
Pole[4] = '*'

# если в игоровом поле появляется мина, значит пользователь наступил на мину и он проиграл

loss = any(map(lambda x: x == '*', Pole))
print(loss) # True -> проигрыш, ибо мы встретили хотябы одну мину на поле

# ---------------------------------------------------------------
