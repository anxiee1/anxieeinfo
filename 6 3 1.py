from random import randint
n = int(input("Введите количество элементов в списке: "))
xount=0
str1 = []

for i in range(n):
    str1.append(randint(-3,5))
print(str1)
suma = 0
for i in range(len(str1)):
    if str1[i] == 0:
        p1 = str1.index((str1[i]))
        break
    elif str1[i] != 0:
        xount+=1
        print("Элемент",xount,"не равен нулю")
    elif xount== len(str1):
        break
str2 = (str1[p1:])
for i in range(len(str2)):
    if str2[i] < 0:
        suma -= str2[i]
    elif str2[i]>0:
        suma += str2[i]
    else:
        suma += 0
print(suma)
