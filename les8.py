# Придумать и обработать исключения на ValueError
try:
    a = float(input("введите число 1: "))
    b = float(input("введите число 2: "))
    print("Ответ: ", a+b)
except ValueError:
    print("Число введено не верно!")
# Придумать и обработать исключения на TypeError
try:
    a = int(1285)
    b = str("23235")
    print(a / b)
except TypeError:
    print("Поменяйте тип объекта")