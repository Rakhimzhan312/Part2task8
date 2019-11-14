a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
if a <= b:
    for a in range(a, b+1):
        print(a, end = ' ')
else:
    print('Ваши введеные числа не совпадают критерии условия')
