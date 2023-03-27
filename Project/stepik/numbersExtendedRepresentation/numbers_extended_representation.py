# экспоненциальное число
# <число>e<целая степень десятки>

a = 5e2
# = 5 * pow(10,2) = 5 * 100 = 500.0

b = 1e-2
# 1 * pow(10,-2) = 0.01

c = 1e-8
# 1 * pow(10, -8) = 0,00000001

# -------------------------------------------------
# десятичная система счисления
'''
123 = 1*pow(10,2) + 2*pow(10,1) + 3*pow(10,0) = 100 + 20 + 3 = 123
'''

# -------------------------------------------------
# двоичная система счисления (схема та же, тоько вместо десяти - двойки)
'''
двоичная '001' = 0*pow(2,2) + 0*pow(2,1) + 1*pow(2,0) = 0 + 0 + 1 = '1' десятичная
двоичная '1101' = 1*pow(2,3) + 1*pow(2,2) + 0*pow(2,1) + 1*pow(2,0) = 8 + 4 + 0 + 1 = '13' десятичная

в Python, перед таким числом прописываем '0b' и пишем наше двоичное число
'0b' говорит о том, что сейчас будет двоичное представление числа
'''
a = 0b001
# 1

b = 0b1101
# 13

с = -0b1111
# -15

bin(13) # '0b1101' преобразование любого десятичного числа в двоичное
# -------------------------------------------------
# шестадцатиричная система счисления (схема та же, тоько вместо десятки/двойки - 16)
'''
16: 0-9, A, B, C, D, E, F
первые 10 чисел обычные, а следующие 6 - буквы (A=10, B=11, C=12, D=13, E=14, F=15)

1A = 1*pow(16,1) + 10*pow(16,0) = 16 + 10 = 26
C2DE = 12*pow(16,3) + 2*pow(16,2) + 13*pow(16,1) + 14*pow(16,0) = 49152 + 512 + 208 + 14 = 49886

в Python, перед таким числом прописываем '0x' 
'''

a = 0x1A
# 26

b = 0xC2DE
# 49886

c = -0x34a
# -842

# -------------------------------------------------
# восьмиричная система счисления

'''
8: 0-7

восьмеричное 27 = 2*pow(8,1) + 7*pow(8,0) = 16 + 7 = 23 десятичное

восьмеричные числа не могут содержать в себе числа > 7
'0o87' - тут есть 8, эта запись НЕВЕРНАЯ

в Python, перед таким числом прописываем '0o' 
'''

a = 0o27
# 23

b = 0o54
# 44

c = -0o777
# -511
