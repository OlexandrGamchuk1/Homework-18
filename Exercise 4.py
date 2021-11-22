import time

def timing(number, file):
    start = time.time()
    for i in range(number):
        def wrapper(f):
            def inner(*args):
                return f(*args)
            return inner

        stop = time.time()
        with open(file, 'a') as file_object:
            file_object.write(f'{i} -> {stop - start}\n')
    return wrapper

@timing(10, 'timing result.txt')
def suma(a, b):
    return a + b

print(suma(2, 3))