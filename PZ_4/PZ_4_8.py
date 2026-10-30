# Ввести N чисел. Посчитать и вывести количество чисел равных нулю

n = input('Введите количество чисел N:')
while type(n) != int:
    try:
        n = int(n)
        if n <= 0:
            print('Количество чисел должно быть больше 0')
            n = input('Введите количество чисел N:')
    except ValueError:
        print('Неправильно!')
        n = input('Введите количество чисел N:')

a = 0
i = 1

while i <= n:
    num = input(f"Введите число {i}:")

    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print('Неправильно!')
            num = input(f"Введите число {i}:")

    if num == 0:
        a += 1

    i += 1
print('Количество чисел равных нулю:', a)