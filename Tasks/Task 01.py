"""Напишете функцию, которая принимает список и возвращает True, если все числа в последовательности уникальны,
в противном случае False.
"""

# Задаем список чисел
numbers = [3, 2, 4, 5, 7, 3, 10, 11, 12]

# Объявляем функцию
def check_uniqueness(numbers):
    
    set_numbers = set(numbers)
    if len(set_numbers) == len(numbers):
        return print('True')
    else:
        return print('False')

# Вызываем функцию
check_uniqueness(numbers)
