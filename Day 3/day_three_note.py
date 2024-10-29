from executing.executing import statement_containing_node

if condition:
    statement
else:
    statement

# modulo
# returns how many reminders of that divisions

# Nested if statement
if condition:
    statement
elif condition:
    statement
else:
    statement

# multiple if statement (if all 3 condition is true all will be executed)
if condition:
    statement
if condition:
    statement
if condition:
    statement

# Logical Operators
 and
 or
 not

weight = 85
height = 1.85

bmi = weight / (height ** 2)

print(f"{bmi}")
# 🚨 Do not modify the values above
# Write your code below 👇
if bmi <= 18.5:
    print("underweight")
elif 18.5 <= bmi <= 25:
    print("normal weight")
elif bmi >= 25:
    print("overweight")
else:
    print("not working")