pairs = [(1, 3), (2, 2), (4, 1)]

def get_second_element(t):
    second_value = t[1]
    return second_value

sorted_pairs = sorted(pairs, key=get_second_element)
print(sorted_pairs)