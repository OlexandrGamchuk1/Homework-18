def decorator_func(func):
    count = 0
    def wrapper(*args):
        nonlocal count
        count += 1
        return f'Sum: {func(*args)}\n' \
               f'The function was called: {count}'
    return wrapper

@decorator_func
def suma(a, b):
    return a + b

print(suma(2, 3))
print(suma(4, 2))