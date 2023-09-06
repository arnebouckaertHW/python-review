# the list is one of python's main ordered collections

# this line of code creates an empty list
nums = []
print(nums)

# this line of code creates a list with 5 integers
nums = [1, 2, 3, 4, 5]
print(nums)

# these lines of code are accessing an element value in the list by using its index
print(nums[1])
nums[4] = 6
print(nums)

# if an attempt is made to access an element that does not exist, an IndexError exception is raised
# print(nums[5])
# nums[-6] = 0

# we may use negative indices in the square brackets
# in the case of this list -5, -4, -3, -2, -1 are the only valid indices
# with -1 being the index for last element in the list and -5 being the index for first element in the list
print(nums[-1])
print(nums[-5])

# the python len function returns the number of elements in a list
print(len(nums))

# this line of code is creating a list of values of mixed types
mixed = [1, "one", 2, "two", 3, "three"]
print(mixed)

# a handy way of stepping through the elements of a list is by using a loop

# While loop
i = 0
while (i < len(mixed)):
    print(mixed[i], end=" ")
    i += 1
print()

# python has built in functions that may be used to manipulate lists

# the append function adds an element to the end of a list
names = []
print(names)

# these lines of code will use the append function to add elements one at a time
names.append("John")
names.append("Paul")
names.append("George")
names.append("Ringo")
print(names, ' - original list')

# these lines of code add multiple elements to the list using a loop
for i in range(1,5):
    names.append(i)
print(names, ' - add multiple elements using a loop')

# this line of code adds a tuple to a list
names.append(('Bob', 'Dylan'))
print(names, ' - add tuple')

# this line of code adds a list to a list
names.append([1, 2])
print(names, ' - add list')

# the insert function may be used to add an element at a specified index
names.insert(0, "Ash")
names.insert(5, 0)
print(names, ' - insert function')

# the extend function may be used to add multiple elements to a list
names.extend(["Han", "Anakin", "Luke", "Han"])
print(names, ' - extend function')

# the reverse function may be used to reverse the order of the elements in a list
names.reverse()
print(names, ' - reverse function')

# the remove function may be used to remove an element from a list (first value found)
names.remove(('Bob', 'Dylan'))
print(names, ' - remove function')

# an error will be generated if the value does not exist in the list
# names.remove([1,2,3])

# only the first occurrence of the value will be removed
names.remove('Han')
print(names, ' - remove function first value only')

# the remove function only removes one element at a time
# to remove a range of elements, a loop must be used
names.reverse()
print(names)
for i in range(0, 5):
    names.remove(i)
print(names, ' - remove function loop')

# the pop function may be used to remove an element from a list and returns the value
# if no index is specified, the last element is removed
last = names.pop()
print(last)
print(names, ' - pop function')

# to remove an element from a specific position in a list use the index as an argument
first = names.pop(0)
print(first)
print(names, ' - pop function by index')

