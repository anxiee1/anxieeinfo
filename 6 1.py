s=input("Введите строку: ")
a=''
for i in s: 
    if i not in a and i != ' ':
        a+=i
print("Отредактированная строка:",a)
