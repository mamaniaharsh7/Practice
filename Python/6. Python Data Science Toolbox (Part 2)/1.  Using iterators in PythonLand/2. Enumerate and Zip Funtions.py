"""
1.
Using enumerate

You're really getting the hang of using iterators, great job!

You've just gained several new ideas on iterators from the last video and one of them is the enumerate() function. Recall that enumerate() returns an enumerate object that produces a sequence of tuples, and each of the tuples is an index-value pair.

In this exercise, you are given a list of strings mutants and you will practice using enumerate() on it by printing out a list of tuples and unpacking the tuples using a for loop.
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Create a list of tuples from mutants and assign the result to mutant_list. Make sure you generate the tuples using enumerate() and turn the result from it into a list using list().
    
    Complete the first for loop by unpacking the tuples generated by calling enumerate() on mutants. Use index1 for the index and value1 for the value when unpacking the tuple.
    
    Complete the second for loop similarly as with the first, but this time change the starting index to start from 1 by passing it in as an argument to the start parameter of enumerate(). Use index2 for the index and value2 for the value when unpacking the tuple.

"""

# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1,value1 in enumerate(mutants):
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)



#==========================================================================================================================================
#==========================================================================================================================================




"""
2.
Using zip

Another interesting function that you've learned is zip(), which takes any number of iterables and returns a zip object that is an iterator of tuples. If you wanted to print the values of a zip object, you can convert it into a list and then print it. Printing just a zip object will not return the values unless you unpack it first. In this exercise, you will explore this for yourself.

Three lists of strings are pre-loaded: mutants, aliases, and powers. First, you will use list() and zip() on these lists to generate a list of tuples. Then, you will create a zip object using zip(). Finally, you will unpack this zip object in a for loop to print the values in each tuple. Observe the different output generated by printing the list of tuples, then the zip object, and finally, the tuple values in the for loop.
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Using zip() with list(), create a list of tuples from the three lists mutants, aliases, and powers (in that order) and assign the result to mutant_data.
    
    Using zip(), create a zip object called mutant_zip from the three lists mutants, aliases, and powers.
    
    Complete the for loop by unpacking the zip object you created and printing the tuple values. Use value1, value2, value3 for the values from each of mutants, aliases, and powers, in that order.

"""

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1,value2,value3 in mutant_zip:
    print(value1, value2, value3)
    
    

#==========================================================================================================================================
#==========================================================================================================================================





"""
3.
Using * and zip to 'unzip'

You know how to use zip() as well as how to print out values from a zip object. Excellent!

Let's play around with zip() a little more. There is no unzip function for doing the reverse of what zip() does. We can, however, reverse what has been zipped together by using zip() with a little help from *! * unpacks an iterable such as a list or a tuple into positional arguments in a function call.

In this exercise, you will use * in a call to zip() to unpack the tuples produced by zip().

Two tuples of strings, mutants and powers have been pre-loaded.
"""


#==========================================================================================================================================


#EXERCISE :

"""
Print the tuples in z1 by unpacking them into positional arguments using the * operator in a print() call.

Because the previous print() call would have exhausted the elements in z1, recreate the zip object you defined earlier and assign the result again to z1.

'Unzip' the tuples in z1 by unpacking them into positional arguments using the * operator in a zip() call. Assign the results to result1 and result2, in that order.

The last print() statements prints the output of comparing result1 to mutants and result2 to powers. Click Submit Answer to see if the unpacked result1 and result2 are equivalent to mutants and powers, respectively.
"""

# Create a zip object from mutants and powers: z1
z1 = zip(mutants,powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants,powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)



#==========================================================================================================================================
#==========================================================================================================================================
