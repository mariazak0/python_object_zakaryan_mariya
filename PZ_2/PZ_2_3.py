a = input("Введите первое число:")
b = input('Введите второе число:')

while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input('Введите первое число:')
while type(b) != float:
    try:
        b = float(b)
    except ValueError:
        print('Неправильно ввели!')
        b = input('Введите второе число:')
# Вычисляем произведение
c = a * b
#Проверяем знак
if c < 0:
    c = c * 8
else:
    c = c * 1.5
print("Результат:", c)