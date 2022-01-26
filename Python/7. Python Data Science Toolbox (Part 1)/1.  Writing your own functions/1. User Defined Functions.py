"""
1.
Single-parameter functions

In the previous exercise, you defined and called the function shout(), which printed out a string concatenated with '!!!'. You will now update shout() by adding a parameter so that it can accept and process any string argument passed to it. Also note that shout(word), the part of the header that specifies the function name and parameter(s), is known as the signature of the function. You may encounter this term in the wild!
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Complete the function header by adding the parameter name, word.
    
    Assign the result of concatenating word with '!!!' to shout_word.
    
    Print the value of shout_word.
    
    Call the shout() function, passing to it the string, 'congratulations'.

"""

# Define shout with the parameter, word
def shout(parameter):
    """Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = parameter + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')


#==========================================================================================================================================
#==========================================================================================================================================



"""
2.
Functions that return single values

You're getting very good at this! Try your hand at another modification to the shout() function so that it now returns a single value instead of printing within the function. Recall that the return keyword lets you return values from functions. Parts of the function shout(), which you wrote earlier, are shown. Returning values is generally more desirable than printing them out because, as you saw earlier, a print() call assigned to a variable has type NoneType.
"""


#==========================================================================================================================================


#EXERCISE :

"""

    In the function body, concatenate the string in word with '!!!' and assign to shout_word.
    
    Replace the print() statement with the appropriate return statement.
    
    Call the shout() function, passing to it the string, 'congratulations', and assigning the call to the variable, yell.
    
    To check if yell contains the value returned by shout(), print the value of yell.


"""

# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word=word+"!!!"

    # Replace print with return
    return (shout_word)

# Pass 'congratulations' to shout: yell
yell=shout('congratulations')

# Print yell
print(yell)

#==========================================================================================================================================
#==========================================================================================================================================
