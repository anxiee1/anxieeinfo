import numpy as np

def find_min_among_max(matrix):
    max_elements = np.max(matrix, axis=1)  # Находим максимальные элементы в каждой строке

    min_among_max = np.min(max_elements)  # Находим минимальный среди максимальных элементов
    min_index = np.where(max_elements == min_among_max)[0][0]  # Находим индекс строки
    row_index = np.where(matrix[min_index] == min_among_max)[0][0]  # Находим индекс столбца

    return min_among_max, min_index, row_index

# Размеры матрицы
M = int(input("Введите M: "))
N = int(input("Введите N: "))

# Создаем матрицу размера M*N со случайными числами от 1 до 10
matrix = np.random.randint(1, 10, size=(M, N))

print("Исходная матрица:")
print(matrix)

min_element, min_index, row_index = find_min_among_max(matrix)

print(f"Минимальный элемент среди максимальных элементов строк: {min_element}")
print("Индекс строки: ",min_index," Индекс столбца:", row_index)
