# Topic Recap: Lists

# 3 Easy Exercises

# Exercise 1 (Easy): List of Squares
# Explanation: Write a Python program that creates a list of squares from 1 to n (where n is a user input).
# Guidance: Use a `for` loop and the `append()` method to add squares to the list.
# Solution:
n = int(input("Enter the value of n: "))
squares = []

for i in range(1, n + 1):
    squares.append(i ** 2)

print(f"List of squares from 1 to {n}: {squares}")

# Example Input:
# Enter the value of n: 5
# Example Output:
# List of squares from 1 to 5: [1, 4, 9, 16, 25]


# Exercise 2 (Easy): Find the Maximum in a List
# Explanation: Write a Python program that finds and prints the maximum number in a given list of integers.
# Guidance: Use the built-in `max()` function to find the maximum number.
# Solution:
numbers = [5, 3, 9, 1, 7, 4]
maximum_number = max(numbers)

print(f"Maximum number in the list: {maximum_number}")

# Example Input:
# (No input required)
# Example Output:
# Maximum number in the list: 9


# Exercise 3 (Easy): Remove Duplicates from a List
# Explanation: Write a Python program that removes duplicates from a list of integers.
# Guidance: Use a loop and the `in` operator to check for duplicates.
# Solution:
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(f"List without duplicates: {unique_numbers}")

# Example Input:
# (No input required)
# Example Output:
# List without duplicates: [1, 2, 3, 4, 5]


# 2 Medium Exercises

# Exercise 4 (Medium): List Reversal
# Explanation: Write a program that reverses a list without using the built-in `reverse()` method or slicing.
# Solution:
numbers = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(f"Reversed list: {reversed_list}")

# Example Input:
# (No input required)
# Example Output:
# Reversed list: [5, 4, 3, 2, 1]


# Exercise 5 (Medium): Merge and Sort Two Lists
# Explanation: Write a program that takes two lists of numbers, merges them into one list, and sorts the resulting list in ascending order.
# Solution:
list1 = [3, 1, 7]
list2 = [8, 4, 2]
merged_list = list1 + list2

# Implementing bubble sort
for i in range(len(merged_list) - 1):
    for j in range(len(merged_list) - i - 1):
        if merged_list[j] > merged_list[j + 1]:
            merged_list[j], merged_list[j + 1] = merged_list[j + 1], merged_list[j]

print(f"Merged and sorted list: {merged_list}")

# Example Input:
# (No input required)
# Example Output:
# Merged and sorted list: [1, 2, 3, 4, 7, 8]


# 1 Hard Exercise

# Exercise 6 (Hard): Rotating a List
# Explanation: Create a program that rotates a list to the right by a specified number of steps.
# - For example, given the list [1, 2, 3, 4, 5] and 2 steps, the result should be [4, 5, 1, 2, 3].
# Solution:
def rotate_list(lst, steps):
    n = len(lst)
    steps = steps % n  # Handle cases where steps are greater than the list length
    rotated_list = lst[-steps:] + lst[:-steps]
    return rotated_list

numbers = [1, 2, 3, 4, 5]
steps = int(input("Enter the number of steps to rotate: "))
rotated_numbers = rotate_list(numbers, steps)

print(f"Rotated list: {rotated_numbers}")

# Example Input:
# Enter the number of steps to rotate: 2
# Example Output:
# Rotated list: [4, 5, 1, 2, 3]