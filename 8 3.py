def digitcount(s):
    if s == '':
        return 0
    elif s[0].isdigit():
        return digitcount(s[1:]) + 1
    else:
        return digitcount(s[1:])
strings = []
for i in range(5):
    string = input("Введите строку: ")
    strings.append(string)

for string in strings:
    count = digitcount(string)
    print(f"Количество цифр в строке '{string}': {count}")
