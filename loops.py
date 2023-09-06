# python supports the for and while loops
# loops are used to execute a block of code multiple times

# the for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

# string
iterable = "987654321"
for i in iterable:
    print(i, end=" ")
print("blastoff!")

# tuple
iterable = (9, 8, 7, 6, 5, 4, 3, 2, 1)
for i in iterable:
    print(i, end=" ")
print("blastoff!")

# list
iterable = [9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in iterable:
    print(i, end=" ")
print("blastoff!")

# dictionary
iterable = dict({"nine": 9, "eight": 8, "seven": 7, "six": 6, "five": 5, "four": 4, "three": 3, "two": 2, "one": 1})
for i in iterable:
    print("%d" % (iterable[i]), end=" ")
print("blastoff!")

# the while loop is used to execute a block of code multiple times as long as a specified condition is true
i = 9
while (i > 0):
    print(i, sep=" ", end=" ")
    # there must be a line of code that changes the condition
    # else the loop will never end
    i -= 1
print("blastoff!")

# only even numbers
i = 8
while (i > 0):
    print(i, sep=" ", end=" ")
    # there must be a line of code that changes the condition
    # else the loop will never end
    i -= 2
print("blastoff!")

i = 9
while (i > 0):
    if(i % 2 == 0):
        print(i, sep=" ", end=" ")
    # there must be a line of code that changes the condition
    # else the loop will never end
    i -= 1
print("blastoff!")

