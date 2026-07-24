'MATPLOTLIB'
'''
-Matplotlib is a python library used for data visulization
-it helps you create graphs, charts and plots to understand datavisualization 
-it is one of the most widely used tools in data analysis and works very well 
with pandas'''

'A.line plot'
'''
-syntax
plt.plot(x, y, color="color", marker="symbol", label="name")'''

#eg line plot 
import matplotlib.pyplot as plt 
x = [1,2,3,4,5]
y=[10,20,30,40,50]

plt.plot(x,y)
plt.title("line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
# plt.savefig("line_chart.png")
plt.show()

#concepts 
'1.plt.plot()'
'''
It is a function from matplotlib.pyplot used to create line graph it connects
data points with a line to show trends or reletionships '''

'2.plt.title()'
'''
-It is a function from matplotlib.pyplot used to set the title of a plot the
title appears at the top of the graph and describe what the chart represents '''

'3.xlabel()'
'''
-It is a function from matplotlib.pyplot used to set the label of the x-axis 
of plot, it tells what the horizontal axis represents'''

'4.ylabel()'
'''
-It is a function from matplotlib.pyplot used to set the label of the y-axis 
of plot, it tells what the vertical  axis represents'''

'5.plt.show()'
'''
-It is functionfrom matplotlib.pyplot used to display the plot on the screen 
-without it your graph may not appear (especially in scripts or some IDEs)
'''
'''
NOTE:
pyplt- One specific submodule(tool) in the matplotlib(toolbox) used for plotting graphs
IDEs - Integrated Development Environment
IDEL - Integrated Development and Learning Environment'''

'6.plt.savefig("figure_name")'
'''
-It is a function from matplotlib.pyplot used to save a plot as an image(.PNG)
or file 
-It lets you export your visulization instead of only showing it on screen'''

'7.plt.grid()'
'''
-plt.grid(True) is a function from matplotlib.pyplot used to diaplay gridlines 
on a plot 
-gridlines makes graph's easier to read by helping you usually aligin values
on the x and y axis '''

'8.plt.legend()'
'''
It is funtion from matplotlib.pyplot used to display labels for different plots in a graph
it shows a smallbox (legend) that explains what each line/bar represents '''






'B.Bar chart()'

'''
-It is a function from matplotlin.pyplot used to create a bar chart
-A bar chart is used to compare values acrross categories
-syntax 
plt.bar(categories, values, color="color", label="name")'''
#eg 
categories=["Apple","Oranges","Strowberry","Pineapple"]
values  =[500,350,400,150]
plt.bar(categories,values,label="Food_Prices")
plt.title("Bar Chart")
plt.xlabel("X-axis Food")
plt.ylabel("Y-axis Prices")
plt.legend()
# plt.savefig("Bar_chart.png")
plt.show()


'C.Scatter plot'
'''
syntax
plt.scatter(x, y, color="color", marker="symbol", label="name")'''

#eg
x2=[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
y2=[1,6,-3,-2,-2,-3,1,-1,-4,1,2,3,5,-2,-3,-4,-3,1,-1,-2,1]
plt.scatter(x2,y2)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
# plt.savefig("scatter_plot.png")
plt.show()

'D.plt.pie()'
'''syntax
plt.pie(values, labels=names, autopct="format")
'''
'''
where, 
x = A list of numbers that determines the size of each pie slice.(data values)
labels = Names displayed on each slice. Default is None (no labels). (labels)
autopct = Displays the percentage value on each slice. Default is None (no percentages).'''
#eg 
labels = ["A","B","C"]
sizes=[30,40,30]
plt.pie(sizes,labels=labels,autopct="%1.1f%%") 
plt.title("Pie Chart")
plt.show()

'''
here
autopact = Displays the percentage value on each slice. Default is None (no percentages)
"%1.1f%%"= how to display the percentage on each pie slice
        1. % - Starts the formatting instruction
        2. 1.- Minimum width of the number ( not required in many cases )
        3..1 - Means show 1 digit after the decimal point #eg 30.0
        4. f - Means floating-point number (a decimal number) # 99.9
        5. %%- Prints the percent (%) symbol

        Why two % signs?
            The first % is used for formatting
            To print an actual %, you must write %%         
        '''

'E.Histogram '
'''
plt.hist() is a Matplotlib function used to create a histogram, which shows how data is 
distributed by grouping values into intervals (called bins)
-syntax
plt.hist(data, bins=number, color="color", label="name")
where ,
x = List or array of numerical data
bins = Number of intervals (groups) to divide the data into (default is 10
'''
#eg 
data = data = [10, 20,20,30,30, 30, 40,]
plt.hist(data,bins=5)
plt.title("Histogram")
plt.show()

'Understand how bin works '
'''
# Easy memory trick
# Find minimum value.
# Find maximum value.
# Calculate range = maximum − minimum.
# Calculate bin width = range ÷ number of bins.
# Create equal intervals (bins).
# Count how many values fall into each interval.
'''

'F.plt.legnd()'
'''
It is funtion from matplotlib.pyplot used to display labels for different plots in a graph
it shows a smallbox (legend) that explains what each line/bar represents'''
#eg line plot
x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [15, 25, 35, 45]

plt.plot(x, y1, label="Sales")
plt.plot(x, y2, label="Profit")
plt.title("legend line chart")

plt.legend()
plt.show()

'G.Marker'
'''
In matplotlib.pyplot markers are symbols used to highlights individual data points in a plot instead 
of just drawing a line marker show exact points on the grapha'''
#eg 
x3=[10,20,30,40,50]
y3=[45,50,35,60,70]
plt.plot(x3,y3,marker="x")
plt.title("marker line chart")
plt.show()

