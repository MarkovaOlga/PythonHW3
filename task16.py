# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Попробуйте использовать метод count(), а также решите задачу с помощью своего алгоритма (без count).
# Замерьте время работы двух алгоритмов и сравните, подумайте, почему оно отличается.
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

input_list = []
list_len = int(input("Введите количество элементов в списке: "))

for i in range(list_len):
    input_list.append(int(input(f"Введите число {i+1}: ")))
print(input_list)
number = int(input("Введите число,которое хотите посчитать в списке: "))

import time

start = time.perf_counter()
count_numbers = input_list.count(number)
print(count_numbers)
end = time.perf_counter()
first_time = end - start


start = time.perf_counter()
count_numbers = 0
for el in input_list:
    if el == number:
        count_numbers += 1
end = time.perf_counter()
second_time = end - start
print(first_time / second_time)

print(count_numbers)
