# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца.

# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# На входе:

# print_operation_table(lambda x, y: x * y, 3, 3)

# На выходе:

# 1 2 3
# 2 4 6 
# 3 6 9

def print_operation_table(operation, num_rows, num_columns):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"ОШИБКА! Размерности таблицы должны быть больше 2!" for x in i])


print_operation_table(lambda x, y: x * y, 3, 3)

def print_operation_table(operation, num_rows, num_columns):
    if num_rows<2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    res = [[operation(row, col) for row in range(1, num_columns + 1)] for col in range(1, num_rows + 1)]

    for i in res:
        print(*[f"{x} " for x in i])


print_operation_table(lambda x, y: x * y, 3, 3)

# ____________________________________________________________________________________________________________________________________

# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу.

# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, 
# если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

# На входе:

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# На выходе:

# Парам пам-пам

def rhythm(str):   
        phrase = str.split()
        list_1 = []
        for word in phrase:
        # word=word.split("-")
            vowels = 0
            for i in word:
                if i in 'аеёиоуыэюя':
                 vowels += 1
            list_1.append(vowels)
        return len(list_1) == list_1.count(list_1[0])


stroka = 'какве-терсме-ётлис-ти'
if " " not in stroka:
    print("Количество фраз должно быть больше одной!")
else:
    if rhythm(stroka):
        print('Парам пам-пам')
    else:
        print('Пам парам')