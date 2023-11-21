"""NUMBER ONE"""

import math
# Allowing the user input their own degree value
degrees = float(input('Enter value in degrees: '))


# math.radians is used to change everything to radians
answer = math.radians(degrees)
# printing out the results of the degrees input
print(answer)


"""NUMBER TWO"""
# CALCULATING AREA OF A PARALLELOGRAM
# Creating the empty list so ican add the numbers the user input
numbers = [] # Creating an empty list in order to append height and length

# allowing the user input the values
height = float(input("Please input the height of the parallelogram: "))
length = float(input("please input the length of the base: "))

# adding the userinput to the list using append
numbers.append(height)
numbers.append(length)

print("The area of the parallelogram is ", math.prod(numbers))

"""NUMBER THREE"""

number = int(input("please input any values so you can get its smallest multiple:"))
factors = list(range(1, number+1)) # Putting the numbers in a list
smallest_multiple = math.prod(factors)

print(factors)
print(f"The smallest multiple of {number} values", smallest_multiple)

"""NUMBER FOUR"""

import numpy as np

array = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
num = 3.1

print("Original array:")
print(array)
print("Checking for complex number:")
print(np.iscomplex(array))
print("Checking for real number:")
print(np.isreal(array))
print("Checking for scalar type:")
print(np.isscalar(num))

"""NUMBER FIVE"""
# Initialising the array
array = np.array([1, 7, 13, 105])
print("Original array:")
print(array) # Printing out the array
print("Size of the memory occupied by the said array:")
print(f"{array.size * array.itemsize} bytes")