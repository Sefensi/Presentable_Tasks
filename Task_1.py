# Нахождение в массиве A[1..N] самого близкого по величине элемента, или списка элементов к заданному числу X
import random


count_of_numbers = int(input("Введите длину массива: "))
list_of_numbers = []

for i in range(count_of_numbers):
    list_of_numbers.append(random.randint(-count_of_numbers, count_of_numbers))
print(list_of_numbers)

finding_number = int(input("Введите число для поиска ближайшего к X: "))
final_number = 0
count_of_final = 0
list_of_finals = []
max_diff = count_of_numbers 
for i in range(len(list_of_numbers)):
    difference = abs(list_of_numbers[i] - finding_number)
    if not difference > max_diff:
        if max_diff == difference:
            list_of_finals.append(list_of_numbers[i])
        else:
            list_of_finals.clear()
            list_of_finals.append(list_of_numbers[i])
        max_diff = difference
        final_number = list_of_numbers[i]
if len(list_of_finals) > 1:
    print(f"Ближайшие к X числа из строки: {list_of_finals} ")
else:
    print(f"Ближайшее число к X = {final_number} ")