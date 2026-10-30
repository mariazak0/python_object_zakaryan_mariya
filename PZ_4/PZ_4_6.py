# Найти и вывести S=1!+2!+3!+4!+...+n(n>1)

n = input('Введите целое число n (n > 1):')
while type(n) != int:
    try:
        n = int(n)
        if n <= 1:
            print('Число должно быть больше 1')
            n = input('Введите целое число n (n > 1):')
    except ValueError:
        print('Неправильно ввели!')
        n = input('Введите целое число n (n > 1):')
a = 0
b = 1
i = 1

while i <= n:
    b *= i
    a += b
    i += 1
print('Сумма факториалов S =',a)