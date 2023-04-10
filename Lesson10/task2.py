def uniq_numbers(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Список має бути типу 'list'")

    if len(numbers) != len(set(numbers)):
        raise ValueError("Список містить неунікальні елементи")

    print("Всі елементи списку унікальні")

# для прикладу наш list не унікальний:
numbers = [1, 2, 3, 3, 4, 5]
uniq_numbers(numbers)

