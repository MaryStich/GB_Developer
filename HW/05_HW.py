# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8

# a = 2
# b = 3


# def f(a, b):
#     count=1
#     result=a
#     while count < b:
#         result*=a
#         count+=1
#     return result

# print(f(a, b))

# ___________________________________________________________________________________________________
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:

# sum(2, 2)
# # 4

a = 22
b = 12


def sum(a, b):
    a += 1
    b -= 1
    if b != 0:
        return sum(a, b)
    return a


print(sum(a, b))

# a = 3
# b = 5

# def sum(a, b):
#     a += 1
#     b -= 1
#     if b != 0:
#         sum(a, b)
#     else:
#         return a

# print(sum(a, b))
