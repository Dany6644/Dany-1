'''a = 1, 2, 3
b=str(a)
print(b)
print(type(b))

a = 1, 5.5,"hello"
b = list(a)
print(b)
print(type(b))


a = int(input('Введите целое число: -'))
if a % 2 == 0:
    print(f'Число {a} является четным')
else:
    print(f'Число {a} является не четным')'''


a = input('Введите строку:')
b = len(a)
print(f'Количество слов в строке: {b}')