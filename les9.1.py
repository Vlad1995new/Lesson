# Пользователь вводит число, нужно узнать делится ли число на 5
print("Введите любое число, что бы узнать делится ли оно на 5:")
a=int(input())
if a % 5 == 0:
    print("Число " + str(a) + " кратно 5")
else:
    print("Число " + str(a) + " не кратно 5")