# Вывести на экран столько элементов ряда Фибоначчи, сколько указал пользователь.
# Например, если на ввод поступило число 6, то вывод должен содержать шесть первых чисел ряда Фибоначчи: 1 2 3 5 8 13.
x = int(input("Введите любое целое число: "))
fib1 = 0
fib2 = 1
n = 1
while n <= x:
    print(fib1+fib2)
    n += 1
    fib3 = fib1 + fib2
    fib2 = fib3
    fib1 = fib3 - fib1
print("Ряд Фибоначчи до ", x,"- го числа")
