from random import randint

# Максимальное cулчайное значение в матрице
max_elem_val = 999

# Размер матрицы
martix_size = 5

# Создаём матицу
matrix = [[randint(0, max_elem_val) for i in range(martix_size)] for j in range(martix_size)]

   
# Вывод матрицы
print('=== Матрица ===')
for row in matrix:
    for elem in row:
        # Просто форматирование для красивого вывода от длины максимального значения
        print(f"{elem:>{len(str(max_elem_val))}}", end=" ")
    print()

# Ввод input()
# разбиение .split()|
# преобразование в числа int() и попуто вычитая 1 для индексов через анонимную функцию lambda;  map(func(), array)
# и запись в переменные 
i, j = map(lambda x: int(x) - 1, input('Введите 2 номера столбцов для смены через пробел\n>>> ').split())

# Для каждого элемента в 2-ух столбцах меняем их местами
for k in range(martix_size):
        matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
      
print(f'=== Матрица после смены местами столбца {i + 1} и {j + 1} ===')
for row in matrix:
    for elem in row:
        # Просто форматирование для красивого вывода от длины максимального значения
        print(f"{elem:>{len(str(max_elem_val))}}", end=" ")
    print()


