# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator(n):
    """Function generates fibonacci numbers."""
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


print(*(fibonacci_generator(10)))
