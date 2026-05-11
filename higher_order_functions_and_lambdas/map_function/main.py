def apply_function_to_list(func, items):
    new_list = list(map(func, items))
    return new_list

def double(x):
    return x * 2

def uppercase(s):
    return s.upper()

doubled = apply_function_to_list(double, [1, 2, 3, 4])
print(doubled)

uppercased = apply_function_to_list(uppercase, ["hello", "world"])
print(uppercased)
