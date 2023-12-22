from random import randint
n = int(input("Введите количество элементов в списке: "))
str1 = []
for i in range(n):
    str1.append(randint(-10,10))
print(str1)
for i in range(len(str1)):
    if str1[i] < 0:
        str1.append(str1[i])
        str1.remove(str1[i])
print(str1)
