"""
1.
Functions with multiple parameters

Hugo discussed the use of multiple parameters in defining functions in the last lecture. You are now going to use what you've learned to modify the shout() function further. Here, you will modify shout() to accept two arguments. Parts of the function shout(), which you wrote earlier, are shown.
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Modify the function header such that it accepts two parameters, word1 and word2, in that order.
    
    Concatenate each of word1 and word2 with '!!!' and assign to shout1 and shout2, respectively.
    
    Concatenate shout1 and shout2 together, in that order, and assign to new_shout.
    
    Pass the strings 'congratulations' and 'you', in that order, to a call to shout(). Assign the return value to yell.

"""

# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1=word1+"!!!"
    
    # Concatenate word2 with '!!!': shout2
    shout2=word2+"!!!"
    
    # Concatenate shout1 with shout2: new_shout
    new_shout=shout1+shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell=shout('congratulations','you')

# Print yell
print(yell)

#==========================================================================================================================================
#==========================================================================================================================================



"""
A brief introduction to tuples

Alongside learning about functions, you've also learned about tuples! Here, you will practice what you've learned about tuples: how to construct, unpack, and access tuple elements. Recall how Hugo unpacked the tuple even_nums in the video:

a, b, c = even_nums

A three-element tuple named nums has been preloaded for this exercise. Before completing the script, perform the following:

    Print out the value of nums in the IPython shell. Note the elements in the tuple.
    In the IPython shell, try to change the first element of nums to the value 2 by doing an assignment: nums[0] = 2. What happens?

Code :
# Unpack nums into num1, num2, and num3
num1,num2,num3=nums

# Construct even_nums
even_nums=(2,num2,num3)
"""


#==========================================================================================================================================
#==========================================================================================================================================




"""
2.
Functions that return multiple values

In the previous exercise, you constructed tuples, assigned tuples to variables, and unpacked tuples. Here you will return multiple values from a function using tuples. Let's now update our shout() function to return multiple values. Instead of returning just one string, we will return two strings with the string !!! concatenated to each.

Note that the return statement return x, y has the same result as return (x, y): the former actually packs x and y into a tuple under the hood!
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Modify the function header such that the function name is now shout_all, and it accepts two parameters, word1 and word2, in that order.
    
    Concatenate the string '!!!' to each of word1 and word2 and assign to shout1 and shout2, respectively.
    
    Construct a tuple shout_words, composed of shout1 and shout2.
    
    Call shout_all() with the strings 'congratulations' and 'you' and assign the result to yell1 and yell2 (remember, shout_all() returns 2 variables!).

"""

# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1=word1+"!!!"
    
    # Concatenate word2 with '!!!': shout2
    shout2=word2+"!!!"
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words=(shout1,shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1,yell2=shout_all('congratulations','you')

# Print yell1 and yell2
print(yell1)
print(yell2)

#==========================================================================================================================================
#==========================================================================================================================================
