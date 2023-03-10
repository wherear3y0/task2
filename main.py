# Задача 5
#
# Создать новый двумерный массив,
# заменив несколько одинаковых подряд идущих строк одним вхождением данной строки.
# (Совпадающие строки – строки, у которых все соответствующие элементы равны друз другу).
#
# Для решения этой задачи необходимо пройти по всем строкам матрицы и сравнить их со следующей строкой.
# Если строки идентичны, то нужно продолжить сравнивать следующие строки до тех пор,
# пока не встретится строка, которая не идентична текущей.
# Затем нужно заменить все эти строки на одну строку и добавить ее в новую матрицу.
# Если строки не идентичны, то нужно просто добавить текущую строку в новую матрицу.

import numpy as np

with open("for_np.txt", "r") as file:
    # Считывание строк из файла и удаление символов перевода строки
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    # Замена запятых на точки в строках
    lines = [line.replace(',', '.') for line in lines]

    # Разбиение строк на элементы и создание матрицы
    matrix = [line.split() for line in lines]

    # Преобразование элементов матрицы в числа
    matrix = [[float(num) for num in row] for row in matrix]

# Вывод матрицы на экран
print("Оригинальная матрица из файла: --> ",matrix, end='\n')

def replace_duplicate_rows(arr):
    new_matrix = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            new_matrix.append(arr[i])
    return new_matrix

new_matrix = replace_duplicate_rows(matrix)
print("Исправленная матрица без дубликатов: --> ",new_matrix, end=' ')

# Запись в файл
with open("new_matrix.txt", "w") as file:
    for row in new_matrix:
        file.write(" ".join(str(num) for num in row) + "\n")