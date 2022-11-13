from random import randint

# Максимальное мулчайное значение в матрице
max_elem_val = 60

# Размер матрицы
martix_size = 5

# Создаём матицу
matrix = [[randint(0, max_elem_val) for i in range(martix_size)] for j in range(martix_size)]

# Инициализируем перемменные для записи (в качестве массива вида [значение, индекс_ряда, индекс_колонки])
min_val, max_val = [matrix[0][0], 0, 0], [matrix[0][0], 0, 0]

# Перебераем циклом для ряда и циклом для каждого элементов нём
for row in matrix: #для каждого ряда
    for elem in row: #для каждого эдемента в ряду

        # Сравнения и перезапись если больше/меньше
        if (elem <= min_val[0]):
            min_val = [elem, matrix.index(row), row.index(elem)]
        if (elem >= max_val[0]):
            max_val = [elem, matrix.index(row), row.index(elem)]

# Вывод матрицы
print('===== Матрица =====')
for row in matrix:
    for elem in row:
        # Просто форматирование для красивого вывода от длины максимального значения
        print(f"{elem:>{len(max_val)}}", end=" ")
    print()

# Вывод минимального и максимального
print(f'Минимальное значение: {min_val[0]}; Индекс ряда: {min_val[1]}; Индекс колонки: {min_val[2]}')
print(f'Максимальное значение: {max_val[0]}; Индекс ряда: {max_val[1]}; Индекс колонки: {max_val[2]}')
    
            

