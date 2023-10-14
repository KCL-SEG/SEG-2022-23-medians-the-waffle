"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        sorted_numbers = list(sorted(numbers))
        median : float
        if len(sorted_numbers) % 2 == 0:
            lower_index = int(len(sorted_numbers) / 2 - 1)
            higher_index = int(len(sorted_numbers) / 2)
            median = (sorted_numbers[lower_index] + sorted_numbers[higher_index]) / 2
        else:
            median = sorted_numbers[int((len(sorted_numbers) - 1) / 2)]
        print(median)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
