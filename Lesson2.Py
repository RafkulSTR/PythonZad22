# n = int(input("Введите число: "))
# i = 2
# rez = 1;
# while (i <= n):
#     rez = rez * i;
#     i = i +1
# print(rez)


# a = int(input("Введите число: "))
# f = 1;
# index = 1;
# prednumber = 0;
# rez = 0;
# if (a > 1):
#     while (a >= rez):
#         rez = f + prednumber
#         prednumber = f
#         f = rez
#         index += 1
# if (a == prednumber):
#     print(index)
# else: print('-1')


# N = int(input('Введите число дней: '))
# Pogoda = []
# j = 0;
# for i in range(0,N):
#     Pogoda.append(int(input('Введите погоду: ')))
#     if Pogoda[i] > 0: minus += 1
    
# print(Dni.sort[-1])


# s = 'ОРРОРОРООРРРРРО'
# n = 0

#print("РРР" in s)
# while 'Р' * n in s:
#     n += 1
# print(n - 1)

# s = [2, 3, 5, 9, 3]
# print(sum(s[1::2]))

# my_list = [1, 1, 2, 0, -1, 3, 4, 4]
# my_set = set(my_list)
# print(my_set)
# ln = len(my_set)
# print (ln)

# my_list = [1, 2, 3, 4, 5]
# k = 3
# copy_list = my_list[-k:] +   my_list[:-k]

# print(copy_list)

# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
# res_list = set()
# for value in dict:
#     for key in value:
#         res_list.add(value[key])
# print(res_list)

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# list = [0, -1, 5, 2, 3, 5, 1, 0, 3]
# count = 0
# for i in range(len(list) - 1):
#     if list[i] < list[i + 1]:
#             count += 1
# print(count)

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# new = 'a a a b c a a d c d d'
# list_new = new.split()
# dict_str = dict()
# str_new = ''
# for value in list_new:
#     if value not in dict_str:
#         dict_str[value] = 1
#         str_new += value
#     else:
#         dict_str[value] +=1;
#         str_new += value + '_' + str(dict_str[value]-1)
#     str_new += ' '
# print(str_new)

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".upper().split()
# mnog = set(str)
# print(mnog)
# print(len(mnog))

# n = int(input())
# max_number = 0
# while n != 0:
#  n = int(input())
#  if max_number < n:
#     max_number = n
# print(max_number)

n = int(input())
max_number = -1
while n != 0:
 n = int(input())
 if max_number < n:
    max_number = n
print(max_number)




    



