# Задача 1
a = float(input("введите число a = "))
b = float(input("введите число b = "))
c = float(input("введите число c = "))
if a + b > c and a + c > b and b + c > a:
    print("треугольник существует")
else:
    print("Такого треугольника не может быть")

# Задача 2
print("Введите Ваш возраст от 0 до 100 лет:")
n = int(input()) # возраст
if n == 1 or n == 21 or n == 31 or n == 41 or n == 51 or n == 61 or n == 71 or n == 81 or n == 91:
    print("Вам", n, "год")
elif n>=2 and n<=4 or n >= 22 and n <= 24 or n >= 32 and n <= 34 or n >= 42 and n <= 44 or n >= 52 and n <= 54 or n >= 62 and n <= 64 or n >= 72 and n <= 74 or n >= 82 and n <= 84 or n >= 92 and n <= 94:
    print("Вам", n, "годa")
elif n >= 1 and n <=99:
    print("Вам", n, "лет")
else:
    print("Невероятно")