def is_positive(n):
    if n > 0:
        return True

def filter_positive(numbers):
    postive_numbers = list(filter(is_positive, numbers))
    return postive_numbers

numbers = [-1, 3, 8, 0, -10]
print(filter_positive(numbers))