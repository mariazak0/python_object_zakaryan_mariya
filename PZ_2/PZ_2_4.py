# Ввести число. Если оно четное, разделить его на 4, если нечетное -
# умножить на 5

# Введите число
num = input('Введите число: ')

while type(num) != int:
    try:
        num = int(num)
    except ValueError:
        print ('Неправильно ввели!')
        num = input('Введите число еще раз: ')
# Проверяем на четность
if num % 2 == 0:
    a = num / 4
else:
    a = num * 5
print('Результат', a)