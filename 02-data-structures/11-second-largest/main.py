
def second_largest(numbers):
    if len(numbers) < 2: 
        return None
    largest = None
    second = None
    for number  in numbers: 
        if largest is None or number > largest:
            second = largest 
            largest = number
        if number < largest and ((second is None) or number > second):
            second = number
    return second


print(second_largest(numbers=[3, 1, 4, 1, 5, 9, 2]))
print(second_largest([10, 10, 9]))
print(second_largest([5]))
print(second_largest([7, 7, 7])) 