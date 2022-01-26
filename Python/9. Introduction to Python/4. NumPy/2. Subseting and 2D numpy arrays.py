"""
1.
Subsetting NumPy Arrays

You've seen it with your own eyes: Python lists and numpy arrays sometimes behave differently. Luckily, there are still certainties in this world. For example, subsetting (using the square bracket notation on lists or arrays) works exactly the same. To see this for yourself, try the following lines of code in the IPython Shell:

x = ["a", "b", "c"]
x[1]

np_x = np.array(x)
np_x[1]

The script in the editor already contains code that imports numpy as np, and stores both the height and weight of the MLB players as numpy arrays.
"""


#==========================================================================================================================================


#EXERCISE :

"""
Subset np_weight_lb by printing out the element at index 50.

Print out a sub-array of np_height_in that contains the elements at index 100 up to and including index 110.
"""

# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

#==========================================================================================================================================
#==========================================================================================================================================


"""
2.
Subsetting 2D NumPy Arrays

If your 2D numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.

# regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]

# numpy
import numpy as np
np_x = np.array(x)
np_x[:,0]

For regular Python lists, this is a real pain. For 2D numpy arrays, however, it's pretty intuitive! The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.

The code that converts the pre-loaded baseball list to a 2D numpy array is already in the script. The first column contains the players' height in inches and the second column holds player weight, in pounds. Add some lines to make the correct selections. Remember that in Python, the first element is at index 0!
"""


#==========================================================================================================================================


#EXERCISE :

"""
Print out the 50th row of np_baseball.

Make a new variable, np_weight_lb, containing the entire second column of np_baseball.

Select the height (first column) of the 124th baseball player in np_baseball and print it out.
"""

# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb=np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])

#==========================================================================================================================================
#==========================================================================================================================================


"""
3.
2D Arithmetic

Remember how you calculated the Body Mass Index for all baseball players? numpy was able to perform all calculations element-wise (i.e. element by element). For 2D numpy arrays this isn't any different! You can combine matrices with single numbers, with vectors, and with other matrices.

Execute the code below in the IPython shell and see if you understand:

import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat

np_baseball is coded for you; it's again a 2D numpy array with 3 columns representing height (in inches), weight (in pounds) and age (in years).
"""


#==========================================================================================================================================


#EXERCISE :

"""
You managed to get hold of the changes in height, weight and age of all baseball players. It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.

You want to convert the units of height and weight to metric (meters and kilograms respectively). As a first step, create a numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.

Multiply np_baseball with conversion and print out the result.
"""

# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball+updated)

# Create numpy array: conversion
conversion=np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball*conversion)

#==========================================================================================================================================
#==========================================================================================================================================
