# Ввести N чисел. Найти и вывести их среднее арифметическое

n = input('Введите количество чисел N:')

while type(n) != int:
    try:
        n = int(n)
        if n <= 0:
            print('Количество чисел должно быть больше 0!')
            n = input('Введите количество чисел N:')
    except ValueError:
        print('Неправильно ввели!')
        n = input('Введите количество чисел N:')
a = 0
i = 1
while i <= n:
    n = input(f'Введите число {i}:')

    while type(n) != int:
        try:
            n = int(n)
        except ValueError:
            print('Неправильно!')
            n = input(f'Введите число {i}:')
    a += n
    i += 1
s = a / n
print('Среднее арифметическое:', s)