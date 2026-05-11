def filter_odds(numbers):
    for n in numbers:
        if n % 2 != 0:
            yield n

def square_numbers(numbers):
    for n in numbers:
        yield n ** 2

def chained_odds_squared(numbers):
    filtered = filter_odds(numbers)
    squared = square_numbers(filtered)
    return squared


result = list(chained_odds_squared(range(10)))
print(result)  # Expected: [1, 9, 25, 49, 81]