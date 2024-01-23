import numpy as np

# create a simple array
a = np.array([1, 2, 3])
print("Simple Array:", a)
# create a 2D array (matrix)
b = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:", b)

# 1D array example
c = np.array([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
print(c)
# 2D array
d = np.array([ ["Spring", "March", "April", "May"], ["Summer", "June", "July", "August"], ["Autumn", "September", "October", "November"], ["Winter", "December", "January", "February"] ])
print(d)
# 3D array
e = np.array([ [ ["room1"],["room2"],["room3"] ], [ ["room1"],["room2"],["room3"] ], [ ["room1"],["room2"],["room3"] ] ])
print(e)

# print out april and august
April = d[0,2]
August = d[1,3]
print("April:", April)
print("August:" , August)

# printing out february, may, and october

print("February:", d[3, 3])
print("May:", d[0, 3])
print("October:", d[2, 2])

# adding arrays together
x = np.array([1,2,3])
z = np.array ([10,20,30])
print(x + z)
# Multiplying arrays together
print(x * z)

# activity 1

# creating an array that holds 4 numbers of my choice
f = np.array([1, 2, 3, 4])

# adding the "first number" and "third number" together
result = f[0] + f[2]
print(result)

# printing second and 4th number
print( f[1])
print( f[3])

#printing out all numbers in one loop
for number in f:
    print(number)

# activity 2

# creating an array with 5 numbers
p = np.array([1,2,3,4,5])

# creating a second array with 3,5,7,9,12
k = np.array([3,5,7,9,12])
#Multiplying the arrays together
print(p * k)
#adding arrays together
print(p + k)
# multiplying the first array by the 3rd number in the second array
result_1 = p * k[2]
print(result_1)









