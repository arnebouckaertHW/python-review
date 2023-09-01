# print function
print("Hello World!")

# print without appending a line separator string to the end using the end parameter
print("Hello World!", end=" ")
print("Hello World!")

# print may be given strings as well as any of the primitive and object types
print(100)
print(True)
print(3.14)

# print may be given multiple arguments
print(100, True, 3.14)

# the default space can be modified and can be made to change to any characters, integer or string using the sep parameter
print(100, True, 3.14, sep="-")

# the sep and end parameters may be used together in one print statement
print(100, True, 3.14, sep="-", end="!")

# the string % modulo operator can be used to format strings
# %s is used to format strings
# %d is used to format integers
# %f is used to format floats
print("\nHello %s %s. You are %d years old." % ("Arne", "Bouckaert", 22))
print("Hello %s %s. You are %.2f years old." % ("Arne", "Bouckaert", 22.5))

# input function
# input function is used to read a line of text from the standard input
# the input function returns a string
first = input("What is your first name? ")
last = input("What is your last name? ")
print(first, last)

age = input("What is your age? ")
print("Hello %s %s. You are %s years old." % (first, last, age))
# this line of code will generate a TypeError because age is a string and not a float
# print("Hello %s %s. You are %.2f years old." % (first, last, age))
print(type(first), type(last), type(age))

# we must typecast the returned object from the input function to the desired type
intage = int(input("What is your age? "))
print("Hello %s %s. You are %d years old." % (first, last, intage))
floatage = float(input("What is your age? "))
print("Hello %s %s. You are %.2f years old." % (first, last, floatage))

# split function
# split function is used to split a string into a list of strings
# if the split function is not given any parameters, it will split the string on whitespace
fname, lname = input("Enter your first and last names separated by a space: ").split()
print(fname, lname)

# if the split function is given a parameter, it will split the string on that parameter
fname, lname, tn = input("Enter your first and last names and telephone separated by a comma: ").split(",")
print("Hello %s %s. Your phone number is %s." % (fname, lname, tn))

# we can take in a variable number of inputs at a time
x = [int(x) for x in input("Enter multiple numbers separated by a space: ").split()]
print("Numbers are: ", x)