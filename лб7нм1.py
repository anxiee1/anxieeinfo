import random
import numpy 
def find_numbers(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    numbers = []
    
    for i in range(row_count):
        for j in range(i+1, col_count):
            numbers.append(matrix[i][j])    
    return numbers

M = random.randrange(4,7)
N = M
k=0
count=0
matrix = numpy.zeros((M, N))
for i in range(M):
    for j in range(N):
        matrix[i][j] = random.randrange(-5,10)
print(matrix)
result = find_numbers(matrix)
#print(result)
for otr in (result):
    if otr<0:
        k+=1
print("Количество отрицательных элементов выше главной диагонали: ",k)
    
