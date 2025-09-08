print("Lesson1-Welcome to Variables!")
# Demo1 - First Variable
# print("=============================")
print("=" * 30)
name = "Elliot"
age = 18
print(name)
print("Student Name:",name)
print(f"Student Name:{name}")
print(f"{name} is {age} years old.")
print(name + " " + "is" + " " + str(age) + " " + "years old.")

#Demo2: Different Data Types
print("=" * 30)
student_name = "John" #string
student_height = 5.8 #float
is_absent = False #boolean

#Demo3: Variables can change
score = 85
print(f"Score: {score}")
score = 90
print(f"Score: {score}")