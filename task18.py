# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

input_list = []
list_len = int(input("Введите количество элементов в списке: "))

for i in range(list_len):
    input_list.append(int(input(f"Введите число {i+1}: ")))
print(input_list)
number = int(input("Введите число, ближайшее к которому нужно найти: "))

dict = {}
for i in range(list_len):
    delt = number-input_list[i]
    if delt < 0:
        delt *= -1
    dict[delt] = input_list[i]
print(dict)
all_keys = list(dict.keys())
# print(all_keys)

index = 0
closest_delt = all_keys[0]
for s in all_keys:
    if s <= closest_delt:
        closest_delt = s
        index_of_delt = index
    index += 1

all_values = list(dict.values())
print(f"Ближайшее число к числу {number} -> {all_values[index_of_delt]}")
