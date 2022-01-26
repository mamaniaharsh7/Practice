"""
1.
Bringing it all together (1)

You've got your first taste of writing your own functions in the previous exercises. You've learned how to add parameters to your own function definitions, return a value or multiple values with tuples, and how to call the functions you've defined.

In this and the following exercise, you will bring together all these concepts and apply them to a simple data science problem. You will load a dataset and develop functionalities to extract simple insights from the data.

For this exercise, your goal is to recall how to load a dataset into a DataFrame. The dataset contains Twitter data and you will iterate over entries in a column to build a dictionary in which the keys are the names of languages and the values are the number of tweets in the given language. The file tweets.csv is available in your current directory.

Be aware that this is real data from Twitter and as such there is always a risk that it may contain profanity or other offensive content (in this exercise, and any following exercises that also use real Twitter data).
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Import the pandas package with the alias pd.
    
    Import the file 'tweets.csv' using the pandas function read_csv(). Assign the resulting DataFrame to df.
    
    Complete the for loop by iterating over col, the 'lang' column in the DataFrame df.
    
    Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count, add 1 to the value corresponding to this key in the dictionary, else add the key to langs_count and set the corresponding value to 1. Use the loop variable entry in your code.

"""

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv("tweets.csv")

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df['lang']

# Iterate over lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
        langs_count[entry]=langs_count[entry]+1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry]=1

# Print the populated dictionary
print(langs_count)



#==========================================================================================================================================
#==========================================================================================================================================



"""
2.
Bringing it all together (2)

Great job! You've now defined the functionality for iterating over entries in a column and building a dictionary with keys the names of languages and values the number of tweets in the given language.

In this exercise, you will define a function with the functionality you developed in the previous exercise, return the resulting dictionary from within the function, and call the function with the appropriate arguments.

For your convenience, the pandas package has been imported as pd and the 'tweets.csv' file has been imported into the tweets_df variable.
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Define the function count_entries(), which has two parameters. The first parameter is df for the DataFrame and the second is col_name for the column name.
    
    Complete the bodies of the if-else statements in the for loop: if the key is in the dictionary langs_count, add 1 to its current value, else add the key to langs_count and set its value to 1. Use the loop variable entry in your code.
    
    Return the langs_count dictionary from inside the count_entries() function.
    
    Call the count_entries() function by passing to it tweets_df and the name of the column, 'lang'. Assign the result of the call to the variable result.

"""

# Define count_entries()
def count_entries (df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry]=langs_count[entry]+1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry]=1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result = count_entries(pd.read_csv("tweets.csv"),'lang')

# Print the result
print(result)

#==========================================================================================================================================
#==========================================================================================================================================
