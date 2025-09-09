# Lesson 2 - Numbers: Integers and Floats
# Follow along as we explore all the concepts!

# 1. INTEGERS - Whole Numbers

# TODO: Create some integer variables
favorite_number = 6
lucky_number = 7
age = 18

# TODO: basic operations
# Addition, subtraction, multiplication, exponent
sum_numbers = favorite_number + lucky_number
dif_numbers = favorite_number - lucky_number
product = favorite_number * lucky_number
power = lucky_number ** 2

print(f"Sum Numbers: {sum_numbers}")
print(f"Difference : {dif_numbers}")
print(f"Product : {product}")
print(f"Power: {power}")


# TODO: Create a variable and change its value
# Start with lives = 3, then lose one: lives = lives - 1
lives = 3
print(f"Player starts with {lives} lives.")
lives = lives - 1 # Long Way
print(f"After losing one: {lives} lives.")
lives -= 1
print(f"After losing one: {lives} lives.")
lives += 1
print(f"After gaining one: {lives} lives.")


# TODO: Demonstrate the difference between / and //
# Use 17 and 5 as examples
a = 15
b = 5
regular_division = a / b
remainder = a % b # % is Modulo Operator
print(f"Regular divison: {regular_division}")
print(f"Integer divison: {a//b}")
print(f"Remainder: {remainder}")









# TODO: Show remainder with 17 % 5
# TODO: Check if a number is even or odd
test_number = 23
if test_number % 2 == 0:
    print(f"{test_number} is even.")
else:
    print(f"{test_number} is odd.")







# TODO: Create some float variables
temp = 98.6
price = 19.99
pi = 3.1459
# TODO: Show float operations
print("Pi:", pi)
print("Pi:" + str(pi))
print(f"Pie:{pi}")
