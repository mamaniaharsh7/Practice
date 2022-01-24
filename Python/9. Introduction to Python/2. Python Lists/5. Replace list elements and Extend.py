"""
:::Replace list elements:::
Replacing list elements is pretty easy. Simply subset the list and assign new values to the subset. You can select single elements or you can change entire list slices at once.

Use the IPython Shell to experiment with the commands below. Can you tell what's happening and why?

x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]
For this and the following exercises, you'll continue working on the areas list that contains the names and areas of different rooms in a house.




:::Extend a list:::
If you can change elements in a list, you sure want to be able to add elements to it, right? You can use the + operator:

x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
You just won the lottery, awesome! You decide to build a poolhouse and a garage. Can you add the information to the areas list?
"""


#==========================================================================================================================================


#EXERCISE :

"""
Update the area of the bathroom area to be 10.50 square meters instead of 9.50.

Make the areas list more trendy! Change "living room" to "chill zone".

Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.

Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.
"""

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1]=10.50

# Change "living room" to "chill zone"
areas[4]="chill zone"

# Add poolhouse data to areas, new list is areas_1
areas_1=areas+["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2=areas_1+["garage", 15.45]
