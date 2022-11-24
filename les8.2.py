print("Введите число, месяц и год рождения")
a=int(input("Число: "))
b=int(input("Месяц: "))
c=int(input("Год: "))
print("Введите чило, месяц и год на сегодняний день")
x=int(input("Число: "))
y=int(input("Месяц: "))
z=int(input("Год: "))
if x>=a and y>=b or y>b:
    print("Ваш возраст: ", z-c)
elif a<x and y<=b or y<b:
    print("Ваш возраст: ", (z-c)-1)