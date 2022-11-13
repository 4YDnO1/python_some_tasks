from math import floor
from random import randint

# Максимальное cулчайное значение в матрице
max_elem_val = 999

# Размер матрицы
martix_size = 5

# Создаём матицу
matrix = [[randint(0, max_elem_val) for i in range(martix_size)] for j in range(martix_size)]

# Инициализируем перемменные для записи 
min_val, P = max_elem_val + 1, 1

# Индекс побочной диагонали (центр) или же если больше центра колонки и больше центра ряда
martix_diagonal_index = floor(martix_size / 2)

# Перебераем циклом для ряда и циклом для каждого элементов нём
for i in range(martix_size): #для каждого ряда
    for j in range(martix_size): #для каждого эдемента в ряду

        # Сравнения и перезапись если меньше
        if (matrix[i][j] <= min_val and i > martix_size - j - 1):
            min_val = matrix[i][j]

# Отдельный перебор последнего ряда в матрице, чтоб не сравнивать в осовных циклах
for elem in matrix[martix_size - 1]:
    # Если отличный от нуля, умножаем
    if (elem != 0):
        P *= elem
        

# Вывод матрицы
print('===== Матрица =====')
for row in matrix:
    for elem in row:
        # Просто форматирование для красивого вывода от длины максимального значения
        print(f"{elem:>{len(str(max_elem_val))}}", end=" ")
    print()

# Вывод минимального значения ниже побочной диагонали (верх-право к низ-лево)
print(f'Минимальное значение ниже побочной диагонали: {min_val}')

# Вывод произведения не нулевых элементов нижней строки матртицы
print(f'Произведение нижних не нулевых элементов матртицы: {P}')
    
            

