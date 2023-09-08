# the python dictionary is a collective of key-value pairs
# a dictionary can be created by placing a sequence of numbers
# within curly braces, separated by commas or by using the dict function
# values in a dictionary can be of any data type and may be repeated
# keys in a dictionary must be unique and may be of any immutable data type
# keys in a dictionary are case sensitive

# this line of code creates an empty dictionary
nums = {}
print(nums)

# this line of code creates a dictionary with 5 key-value pairs
nums = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print(nums)

# this line of code is creating the same dictionary 
# using the dict function
nums = dict({1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'})
print(nums)

# these lines of code are accessing a value 
# in the dictionary by using its key
print(nums[1])
nums[4] = 'six'
print(nums)

# if an attempt is made to access a key that does not exist,
# a KeyError exception is raised
# print(nums[6])

# the python len function tells the number of key-value pairs in a dictionary
print(len(nums))

# this line of code is creating a dictionary of values of mixed types
mixed_values = {1: 1, 2: 'two', 3: 3, 4: 'four', 5: 5}
print(mixed_values)

# this line of code is creating a dictionary of keys of mixed types
mixed_keys = {1: 1, 'one': 1, 2: 2, 'two': 2, 3: 3, 'three': 3}
print(mixed_keys)

# a very handy way to step through the keys of a dictionary
# is by using a for loop
for key in nums:
    print(key, end="")
print()

# these lines of code are using a for loop to
# step through the values of a dictionary
for val in nums.values():
    print(val, end="")
print()

# these lines of code are using a for loop to
# step through the key-value pairs of a dictionary
for key, val in nums.items():
    print(key, val, end=" ")
print()

# a very handy way to step through the values of a dictionary
# is by using a while loop
i = 1
while (i <= len(nums)):
    print(nums[i], end="")
    i += 1
print()

# python has inbuilt functions that may be used to 
# manipulate dictionaries

# the get function returns the value associated with a key
print(nums.get(1))
print(nums)

# the pop function removes a key-value pair from a dictionary
nums.pop(4)
print(nums, " - pop function")

# the popitem function removes the last key-value pair from a dictionary
nums.popitem()
print(nums, " - popitem function")

# the update function updates a key-value pair of a dictionary
nums.update({3: 'python'})
print(nums, " - update function")

# the clear function removes all key-value pairs from a dictionary
nums.clear()
print(nums, " - clear function")

