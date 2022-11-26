# Есть пятизначное натуральное число. Найдите его наибольшую цифру.
# Например: введено число 76458, наибольшая цифра в нём 8.
Chislo1 = str(input("Введите пятизначное натуральное число: "))
a = int(Chislo1[0])
b = int(Chislo1[1])
c = int(Chislo1[2])
d = int(Chislo1[3])
e = int(Chislo1[4])
if a >= b and a >= c and a >= d and a >= e:
    print(a)
elif b >= a and b >= c and b >= d and b >= e:
    print(b)
elif c >= a and c >= b and c >= d and c >= e:
    print(c)
elif d >= a and d >= b and d >= c and d >= e:
    print(d)
elif e >= a and e >= b and e >= c and e >= d:
    print(e)
else:
    print()