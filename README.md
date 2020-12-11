# Machine Learning Tasks 2020


My answers to the tasks below can be found in the Jupyter Notebook file All_Tasks_Machine_Learning.ipynb

1. October 5th, 2020: Write a Python function called sqrt2 that calculates and
prints to the screen the square root of 2 to 100 decimal places. Your code should
not depend on any module from the standard library1 or otherwise. You should
research the task first and include references and a description of your algorithm.

Task 1, I did a lot of draft work but had to resort to stackoverflow



2. November 2nd, 2020: The Chi-squared test for independence is a statistical
hypothesis test like a t-test. It is used to analyse whether two categorical variables
are independent. The Wikipedia article gives the table below as an example [4],
stating the Chi-squared value based on it is approximately 24.6. Use scipy.stats
to verify this value and calculate the associated p value. You should include a short
note with references justifying your analysis in a markdown cell.
A B C D Total
White collar 90 60 104 95 349
Blue collar 30 50 51 20 151
No collar 30 40 45 35 150
Total 150 150 200 150 650
1By the standard library, we mean the modules and packages that come as standard with Python.
Anything built-in that can be used without an import statement can be used.

Task 2, I had researched the possible solutions in scipy.stats documentation, but again I found the best source of information and help was on stackoverflow. 


3. November 16th, 2020: The standard deviation of an array of numbers x is
calculated using numpy as np.sqrt(np.sum((x - np.mean(x))**2)/len(x)) .
However, Microsoft Excel has two different versions of the standard deviation
calculation, STDEV.P and STDEV.S . The STDEV.P function performs the above
calculation but in the STDEV.S calculation the division is by len(x)-1 rather
than len(x) . Research these Excel functions, writing a note in a Markdown cell
about the difference between them. Then use numpy to perform a simulation
demonstrating that the STDEV.S calculation is a better estimate for the standard
deviation of a population when performed on a sample. Note that part of this task
is to figure out the terminology in the previous sentence.

Task 3, I was able to answer this from websites and blogs I found on google, and from my own experience of Excel.

4. November 30th, 2020: Use scikit-learn to apply k-means clustering to
Fisher’s famous Iris data set. You will easily obtain a copy of the data set online. Explain in a Markdown cell how your code works and how accurate it might be, and then explain how your model could be used to make predictions of species of iris.

Task 4, I found best source of help to answering this question was on Youtube as others had done step by step walk through of the task.
