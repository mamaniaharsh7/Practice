"""
1.
Line plot 

With matplotlib, you can create a bunch of different plots in Python. The most basic plot is the line plot. A general recipe is given here.

import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

In the video, you already saw how much the world population has grown over the past years. Will it continue to do so? The world bank has estimates of the world population for the years 1950 up to 2100. The years are loaded in your workspace as a list called year, and the corresponding populations as a list called pop.

This course touches on a lot of concepts you may have forgotten, so if you ever need a quick refresher, download the Python for data science Cheat Sheet and keep it handy!
"""


#==========================================================================================================================================


#EXERCISE :

"""
print() the last item from both the year and the pop list to see what the predicted population for the year 2100 is. Use two print() functions.

Before you can start, you should import matplotlib.pyplot as plt. pyplot is a sub-package of matplotlib, hence the dot.

Use plt.plot() to build a line plot. year should be mapped on the horizontal axis, pop on the vertical axis. Don't forget to finish off with the show() function to actually display the plot.
"""

# Print the last item from year and pop
print(year[-1])
print(pop[-1])


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)

# Display the plot with plt.show()
plt.show()

#==========================================================================================================================================
#==========================================================================================================================================


"""
2.
Scatter Plot 

When you have a time scale along the horizontal axis, the line plot is your friend. But in many other cases, when you're trying to assess if there's a correlation between two variables, for example, the scatter plot is the better choice. Below is an example of how to build a scatter plot.

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show()

Let's continue with the gdp_cap versus life_exp plot, the GDP and life expectancy data for different countries in 2007. Maybe a scatter plot will be a better alternative?

Again, the matplotlib.pyplot package is available as plt.
"""


#==========================================================================================================================================


#EXERCISE :

"""
Change the line plot that's coded in the script to a scatter plot.

A correlation will become clear when you display the GDP per capita on a logarithmic scale. Add the line plt.xscale('log').

Finish off your script with plt.show() to display the plot.
"""

# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

#==========================================================================================================================================
#==========================================================================================================================================
