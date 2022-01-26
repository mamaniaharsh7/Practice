"""
1.
Processing large amounts of Twitter data

Sometimes, the data we have to process reaches a size that is too much for a computer's memory to handle. This is a common problem faced by data scientists. A solution to this is to process an entire data source chunk by chunk, instead of a single go all at once.

In this exercise, you will do just that. You will process a large csv file of Twitter data in the same way that you processed 'tweets.csv' in Bringing it all together exercises of the prequel course, but this time, working on it in chunks of 10 entries at a time.

If you are interested in learning how to access Twitter data so you can work with it on your own system, refer to Part 2 of the DataCamp course on Importing Data in Python.

The pandas package has been imported as pd and the file 'tweets.csv' is in your current directory for your use.

Be aware that this is real data from Twitter and as such there is always a risk that it may contain profanity or other offensive content (in this exercise, and any following exercises that also use real Twitter data).
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Initialize an empty dictionary counts_dict for storing the results of processing the Twitter data.
    Iterate over the 'tweets.csv' file by using a for loop. Use the loop variable chunk and iterate over the call to pd.read_csv() with a chunksize of 10.
    In the inner loop, iterate over the column 'lang' in chunk by using a for loop. Use the loop variable entry.

"""


# Initialize an empty dictionary: counts_dict
counts_dict={}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv',chunksize=10) :

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)




#==========================================================================================================================================
#==========================================================================================================================================




"""
2.
Extracting information for large amounts of Twitter data

Great job chunking out that file in the previous exercise. You now know how to deal with situations where you need to process a very large file and that's a very useful skill to have!

It's good to know how to process a file in smaller, more manageable chunks, but it can become very tedious having to write and rewrite the same code for the same task each time. In this exercise, you will be making your code more reusable by putting your work in the last exercise in a function definition.

The pandas package has been imported as pd and the file 'tweets.csv' is in your current directory for your use.
"""


#==========================================================================================================================================


#EXERCISE :

"""

    Define the function count_entries(), which has 3 parameters. The first parameter is csv_file for the filename, the second is c_size for the chunk size, and the last is colname for the column name.
    
    Iterate over the file in csv_file file by using a for loop. Use the loop variable chunk and iterate over the call to pd.read_csv(), passing c_size to chunksize.
    
    In the inner loop, iterate over the column given by colname in chunk by using a for loop. Use the loop variable entry.
    
    Call the count_entries() function by passing to it the filename 'tweets.csv', the size of chunks 10, and the name of the column to count, 'lang'. Assign the result of the call to the variable result_counts.

"""


# Define count_entries()
def count_entries(csv_file,c_size,colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file,chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv',10,'lang')

# Print result_counts
print(result_counts)



#==========================================================================================================================================
#==========================================================================================================================================
