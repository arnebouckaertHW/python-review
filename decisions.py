# expressions in python evaluate to true or false
# expressions use the comparison operators: 
# ==, !=, <, >, <=, >=

x = 4

print(x < 5)
print(x > 5)
print(x == 5)
print(x != 5)

# python supports the if, if-else, if-elif-else statements
# and nested decision structures

# if decision structure
if (x < 5):
    print("x is less than 5 is true.")
    
# shorthand if decision structure
# the shorthand version may only be used if there is only one line of code in the if block
if (x < 5): print("x is less than 5 is true.")

# if-else decision structure
# the else block is executed when the statement is false, when the statement is true the if block is executed
if (x == 5):
    print("x is equal to 5 is true.")
else:
    print("x is equal to 5 is false.")

# shorthand if-else decision structure
# the shorthand version may only be used if there is only one line of code in the if and else blocks
print("x is equal to 5 is true.") if (x == 5) else print("x is equal to 5 is false.")

# if-elif-else decision structure
# it tests multiple conditions
# the codeblock given to the condition that is true is executed, 
# if none of the conditions are true, the else block is executed
if (x > 5):
    print("x is greater than 5 is true.")
elif (x == 5):
    print("x is equal to 5 is true.")
else:
    print("None of the conditions are true.")

if (x > 5):
    print("x is greater than 5 is true.")
elif (x == 5):
    print("x is equal to 5 is true.")
elif (x < 5):
    print("x is less than 5 is true.")
else:
    print("None of the conditions are true.")

if (x > 5):
    print("x is greater than 5 is true.")
elif (x == 5):
    print("x is equal to 5 is true.")
elif (x < 5):
    print("x is less than 5 is true.")
elif (x != 5):
    # this code block will never be executed because the previous elif condition is true
    print("x is not equal to 5 is true.")
else:
    print("None of the conditions are true.")

# nested decision structures
# decision structures can be nested inside of each other
# the inner decision structure is executed only when the outer decision structure is true
if (x < 5):
    print("x is less than 5 is true.")
    if (x != 5):
        print("x is not equal to 5 is true.")

# comparison operators can be chained together
a = 5
b = 10
c = 15

if (a < b < c):
    print("b is greater than a and less than c.")

# python supports the match-case decision structure
# this decision structure is useful when many conditions need to be tested
# the match-case decision structure is only available in python 3.10 and above
# the match-case decision structure is similar to the switch-case decision structure in other languages
grade = 'A'

match grade:
    case 'A':
        print("Super work!")
    case 'B':
        print("Good job!")
    case 'C':
        print("You made it.")
    case 'D', 'F':
        print("Oh, dear ...")
    case _:
        print("Invalid grade.")

# 3. rewrite to use if-elif-else decision structure
if (grade == 'A'):
    print("Super work!")
elif (grade == 'B'):
    print("Good job!")
elif (grade == 'C'):
    print("You made it.")
elif (grade == 'D' or grade == 'F'):
    print("Oh, dear ...")
else:
    print("Invalid grade.")

# python supports the ternary operator
result = 'x is equal to 5 is true.' if (x == 5) else 'x is equal to 5 is false.'
print(result)
print(('x is equal to 5 is true.' if (x == 5) else 'x is equal to 5 is false.'))

# the ternary operator may be written using tuples
# (false value, true value) [condition]
# x = 5
result = ('x is equal to 5 is false.', 'x is equal to 5 is true.') [x == 5]
print(result)

# the ternary operator may be written using dictionaries
# {True: true value, False: false value} [condition]
result = {True: 'x is equal to 5 is true.', False: 'x is equal to 5 is false.'} [x == 5]
print(result)

# logical operators
# and, or, not
num = 150

# and operator
# both conditions must be true for the expression to be true
if (num >= 1 and num <= 100):
    print("num is between 1 and 100.")
else:
    print("num is not between 1 and 100.")

# or operator
# one of the conditions must be true for the expression to be true
if (num < 1 or num > 100):
    print("num is not between 1 and 100.")
else:
    print("num is between 1 and 100.")

foundIt = False

# this if-else structure tests if foundIt is false
if (not foundIt):
    print("foundIt is false.")
else:
    print("foundIt is true.")