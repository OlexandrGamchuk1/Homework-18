function_list = []

def add_func(f):
    function_list.append(f)
    return f

@add_func
def suma(a, b):
    return a + b

print(function_list)