def process_numbers(numbers):
    def square_and_add_five(x):
        return x ** 2 + 5
    processed_numbers_list = []
    for num in numbers:
        processed_numbers = square_and_add_five(num)
        processed_numbers_list.append(processed_numbers)
    return processed_numbers_list    
    
output = process_numbers([1, 2, 3])
print(output)
