def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = int(input('Введите длину последовательности: '))

for num in fibonacci(n):
    print(num, end=' ')
