##Queren's Homework - NumPy###

#Import numpy and print the version number
import numpy as np


print(f"NumPy Version: {np.__version__}")
#2. Create a 1D array of numbers from 0 to 9
array_1d = np.arange(10)

print(array_1d)

#3. Import iris dataset with text intact

#Define url
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# I saw that dtype=object will get the file format in the more intact way
iris = np.genfromtxt(url, delimiter=',', dtype=None, encoding='utf-8')

# Print the first 5 rows
print(iris[:5])


#4. Find the position of the first occurrence > 1.0 in petalwidth in the 4th column
#Define url
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Load data
iris = np.genfromtxt(url, delimiter=',', dtype=None, encoding='utf-8')

# Extract the 4th column (petal width). When I printed this alone, I saw that the values are floats.
petalwidth = np.array([row[3] for row in iris])

# Create a boolean mask for values greater than 1.0. Masks are great for boolean separation
mask = petalwidth > 1.0

# np.argmax() returns the index of the first True value
position = np.argmax(mask)

print(f"The first occurrence of a value > 1.0 is at position: {position}")

#5. Replace values greater than 30 and less than 10
# Input
np.random.seed(100)
a = np.random.uniform(1, 50, 20)
print(f"Input:\n {a}")

# Clip function to select the values between a minimum of 10 and a maximum of 30, inclusive
b = np.clip(a, a_min=10, a_max=30)
 #I did not like that the floating numbers were so big, so I changed it too.

final_array = np.round(b, 2)#Rounding the floating numbers

print(f"\nClipped and rounded array:\n {final_array}")