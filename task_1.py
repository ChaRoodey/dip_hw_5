def gen(n:int):
    for i in range(1, n + 1):
        yield i ** 2


r = int(input('Введите конечное число: '))
a = (i ** 2 for i in range(1, r + 1))

for i, num in enumerate(gen(r), start=1):
    print(f'Функция: {i} ** 2 = {num}')

for i, num in enumerate(a, start=1):
    print(f'Генератор: {i} ** 2 = {num}')
