"""
Задача 34: 
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке

Ввод:                                       Вывод:
пара-ра-рам рам-пам-папам па-ра-па-дам      Парам пам-пам
"""


# # 1 вариант (через цикл for)

# text = input("Введите стихотворение: ").lower().split()     # <class 'list'> ввожу текст, перевожу все в нижний 
#                                                                 # регистр, разделяю на элементы списка пробелом 
# rifma = list()                                              # создаю пустой список для проверки на рифму
# for i in text:                                              # циклом по элементам списка 
#     count = 0                                               # счетчик количества 'a'
#     for j in i:                                             # циклом по элементу списка (проверка букв - j)
#         if j == 'а':                                     
#             count += 1
#     rifma.append(count)                                     # [4, 4, 4] заполняю список rifma результатами count                            
# if len(set(rifma)) == 1:                                        # <class 'int'> rifma преобразую в множество set(), и у 
#                                                                 # и узнаю количество элементов множенства len()
#     print("Парам пам-пам")                                  # если len(set(rifma)) == 1:, то в множестве 1 уникальный элемент
# else:
#     print("Пам парам")                                      # если len(set(rifma)) != 1, то множестве несколько элементов
#                                                                 # рифмы нет 


# # 2 вариант (через функцию)

# def f(rep):                                                # функция f принимает rep(text) - можно называть по разному
#     return sum(1 for i in rep if i in 'а')                 # возвращает сумму повторов (1) буквы 'a' в rep(text)
    
# text = input("Введите стихотворение: ").lower().split()    
# t = f(text[0])                                              # <class 'int'> в переменную t записала результат вызова f для индекса 0
                                             
# if all([f(i) == t for i in text]):                          # функция all для всех вызовов фукнции f, если все True
#     print("Парам пам-пам")
# else:
#     print("Пам парам")


# # 3 вариант (через lambda)

# text = input("Введите стихотворение: ").lower().split()     # ввожу текст, перевожу все в нижний регистр,
#                                                                 # разделяю на элементы списка пробелом <class 'list'>
# f = lambda x: sum(1 for i in x if i in 'а')                 # x-элементы списка, i-элементы (элемента)-буквы, 1-счетчик sum
#                                                                 # lambda возвращет (return) количество повторов 'a' <class 'int'>
# t = f(text[0])
# if all([f(i) == t for i in text]):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")


# # 4 вариант (со всеми гласными)

# stroka = 'пара-ра-рам рам-пaм-папам па-ра-па-дам'
# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka.split()
# if len(phrases) < 2:                                                # проверка на количество фраз, чтобы их во фразе было >1
#     print("Количество фраз должно быть больше одной!")
# else:
#     countVowels = []

# for i in phrases:                                                  # list.comprehension
#     countVowels.append(len([x for x in i if x.lower() in vowels])) 
# # print(countVowels)                                               # [4, 3, 4]
# # print(countVowels[0])                                            # 4
# # print(len(countVowels))                                          # 3
# # print(countVowels.count(countVowels[0]))                         # 2
# if countVowels.count(countVowels[0]) == len(countVowels):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")

"""
list.comprehension
for i in phrases:
    countVowels.append(len([x for x in i if x.lower() in vowels]))  # если разложить строки list.comprehension, 
                                                                    # то в обычном виде код будет выглядеть так
for i in phrases:
    list=[]
    for x in i:
        if x.lower() in vowels:
        list.append(x)            # list = ['a','a','a']
            
    countVowels.append(len(list)
    
countVowels.append(len([x for x in i if x.lower() in vowels]))  # эта строка звучит: в список countVowels, добавляем длину списка.comprehension 
                                                                # в которые сохраняем те буквы, которые есть в списке vowels
"""


"""
Задача 36: 
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.

Ввод:                                           Вывод:
print_operation_table(lambda x, y: x * y)       1 2 3 4 5 6
                                                2 4 6 8 10 12
                                                3 6 9 12 15 18
                                                4 8 12 16 20 24
                                                5 10 15 20 25 30
                                                6 12 18 24 30 36 
"""

# # 1 вариант

# def print_operation_table(operation, num_rows = 6, num_columns = 6):
#     for i in range(1, num_rows + 1):
#         table=[]
#         for j in range(1, num_columns +1):
#             table.append(str(operation(i, j)))          # str - т.к. список строк(многомерный массив)
#         print('\t'.join(table))                         # .join обратная split() список превращает в строку 
#                                                         # '\t'табуляция
        
# print_operation_table(lambda x, y: x * y)  


# # 2 вариант 

# def print_operation_table(operation, num_rows = 15, num_columns = 15):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:                                                                   # '  ' разделитель между элементами
#         print('\t'.join([str(i) for i in range(1, num_columns + 1)]))       # первая строка просто заполняется 1,2,3,4,5,6
#         for i in range(2, num_rows + 1):
#             print(i, end = '\t')                      # print(i, end = '\t') означает, что следующий i будет через 'таб'
#             for j in range(2, num_columns + 1):
#                 print(operation(i, j), end = '\t')
#             print()                                   # перенос строки после каждого оборота цикла (140 строка)

# print_operation_table(lambda x, y: x * y)

