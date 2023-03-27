a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = "python"

z = zip(a, b)
print(next(z)) # (1, 5)
print(next(z)) # (2, 6)

print(list(z)) # [(1, 5), (2, 6), (3, 7), (4, 8)]

z2 = zip(a, b, c)
#print(list(z2)) # [(1, 5, 'p'), (2, 6, 'y'), (3, 7, 't'), (4, 8, 'h')]
#print(*list(z2)) # (1, 5, 'p') (2, 6, 'y') (3, 7, 't') (4, 8, 'h')

t1, t2, t3 = zip(*list(z2)) #t1, t2, t3 = zip(*z2)
print(t1, t2, t3, sep="\n")
# (1, 2, 3, 4)
# (5, 6, 7, 8)
# ('p', 'y', 't', 'h')

# ----------------------------------------------------------

x = iter([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(*zip(x, x, x))
# (1, 2, 3) (4, 5, 6) (7, 8, 9)

s = ['Москва', 'Уфа', 'Тула', 'Самара', 'Омск', 'Воронеж', 'Владивосток', 'Лондон', 'Калининград', 'Севастополь']
z = zip(*[iter(s)]*3)

for el in z:
    print(*el)
# Москва Уфа Тула
# Самара Омск Воронеж
# Владивосток Лондон Калининград

# ----------------------------------------------------------
