def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

n1 = int(input("Число Фибоначчи с номером: "))
n2 = int(input("Число Фибоначчи с номером: "))
n3 = int(input("Число Фибоначчи с номером: "))
n4 = int(input("Число Фибоначчи с номером: "))
n5 = int(input("Число Фибоначчи с номером: "))

fib1 = fib(n1)
fib2 = fib(n2)
fib3 = fib(n3)
fib4 = fib(n4)
fib5 = fib(n5)

print(f"Число Фибоначчи с номером {n1}: {fib1}")
print(f"Число Фибоначчи с номером {n2}: {fib2}")
print(f"Число Фибоначчи с номером {n3}: {fib3}")
print(f"Число Фибоначчи с номером {n4}: {fib4}")
print(f"Число Фибоначчи с номером {n5}: {fib5}")
