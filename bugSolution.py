def my_function(a, b):
    if a < 0 or b < 0:
        raise ValueError("Negative numbers not allowed.")
    if a > b:
        return a
    return b

print(my_function(5, 2))  # Output: 5
print(my_function(2, 5))  # Output: 5

try:
    print(my_function(-10, 10)) # Raises ValueError
except ValueError as e:
    print(e)  # Output: Negative numbers not allowed.