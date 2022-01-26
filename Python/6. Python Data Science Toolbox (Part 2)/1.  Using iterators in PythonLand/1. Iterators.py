"""
1.
Iterating over iterables (1)

Great, you're familiar with what iterables and iterators are! In this exercise, you will reinforce your knowledge about these by iterating over and printing from iterables and iterators.

You are provided with a list of strings flash. You will practice iterating over the list by using a for loop. You will also create an iterator for the list and access the values from the iterator.
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Create a for loop to loop over flash and print the values in the list. Use person as the loop variable.
    Create an iterator for the list flash and assign the result to superhero.
    Print each of the items from superhero using next() 4 times.

"""


# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for x in flash:
    print(x)


# Create an iterator for flash: superhero
superhero=iter(flash)

# Print each item from the iterator
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))



#==========================================================================================================================================
#==========================================================================================================================================




"""
2.
Iterating over iterables (2)

One of the things you learned about in this chapter is that not all iterables are actual lists. A couple of examples that we looked at are strings and the use of the range() function. In this exercise, we will focus on the range() function.

You can use range() in a for loop as if it's a list to be iterated over:

for i in range(5):
    print(i)

Recall that range() doesn't actually create the list; instead, it creates a range object with an iterator that produces the values until it reaches the limit (in the example, until the value 4). If range() created the actual list, calling it with a value of 10^{100} may not work, especially since a number as big as that may go over a regular computer's memory. The value 10^{100} is actually what's called a Googol which is a 1 followed by a hundred 0s. That's a huge number!

Your task for this exercise is to show that calling range() with 10^{100} won't actually pre-create the list.
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Create an iterator object small_value over range(3) using the function iter().
    Using a for loop, iterate over range(3), printing the value for every iteration. Use num as the loop variable.
    Create an iterator object googol over range(10 ** 100).

"""

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for x in range(3) :
    print(x)


# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))


#==========================================================================================================================================
#==========================================================================================================================================



"""
3.
Iterators as function arguments

You've been using the iter() function to get an iterator object, as well as the next() function to retrieve the values one by one from the iterator object.

There are also functions that take iterators and iterables as arguments. For example, the list() and sum() functions return a list and the sum of elements, respectively.

In this exercise, you will use these functions by passing an iterable from range() and then printing the results of the function calls.
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Create a range object that would produce the values from 10 to 20 using range(). Assign the result to values.
    Use the list() function to create a list of values from the range object values. Assign the result to values_list.
    Use the sum() function to get the sum of the values from 10 to 20 from the range object values. Assign the result to values_sum.

"""

# Create a range object: values
values = range(10,21)

# Print the range object
print(values)

# Create a list of integers: values_list
values_list = list(values)

# Print values_list
print(values_list)

# Get the sum of values: values_sum
values_sum = sum(values)

# Print values_sum
print(values_sum)




#==========================================================================================================================================
#==========================================================================================================================================

