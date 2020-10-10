"""squareroot.py is a program that takes a positive floating-point number as input and outputs an approximation of its square root.
it achieves this by use of a function called sqrt. An output example would be The square root of 14.5 is approx. 3.8."""


#BELOW IN THE COMMENTS IS MY ORIGINAL SOLUTION TO THE NEWTON'S THEORY QUESTION.
#THEN I REALIZED IT DIDN'T ANSWER THE QUESTION AS IT USES PYTHON'S INBUILT FUNCTION
#PYTHON'S math.sqrt INBUILT FUNCTION IS THE EASIEST WAY TO GET THE SQUARE ROOT.
#IT CAN BE ROUNDED DOWN WITH THE INBUILT round FUNCTION.

"""
import math #import math module to access square root calculation
def sqrt(myinput):
    #sqrt function takes and validates a user number input and finds approximate square root to nearest 1 decimal point utilizing and rounding math sqrt function
    while True: #use of while loop with exception handling to ensure user inputs either a float or an integer
        try:
            myinput = float(myinput) #convert input from string to a float, as want to initially make it possible for input to accept int or float input
            myresult = round(math.sqrt(myinput),1) #combining round function to just return maximum of one decimal place from calculated square root
            break
        except ValueError: #use of error handling to prompt user to enter number
            print("Not a valid number! Please try again ...") 
            myinput = input("Please enter a positive number e.g. 14.5") #ask user for input
    return myresult
myinput = input("Please enter a positive number e.g. 14.5:") #ask user for input
print("The square root of", myinput, "is approx." , sqrt(myinput))
"""


#https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
#I have taken the code supplied on this website, see quoted below, and edited this code to take input / handle errors and round
"""
def mySqrt(x):
    r = x
    precision = 10 ** (-10)
    
    while abs(x - r * r) > precision:
        r = (r + x / r) / 2
        
    return r
"""


#my square root work last semester
"""
def sqrt(myinput):
    while True: #use of while loop with exception handling to ensure user inputs either a float or an integer
        try:
            myinput = float(myinput) #convert input from string to a float, as want to initially make it possible for input to accept int or float input

            r = myinput
            precision = 10 ** (-10)
            
            while abs(myinput - r * r) > precision:
                r = (r + myinput / r) / 2
                
            return round(r,1)

        except ValueError: #use of error handling to prompt user to enter number
            print("Not a valid number! Please try again ...") 
            myinput = input("Please enter a positive number e.g. 14.5") #ask user for input
    return myresult


myinput = input("Please enter a positive number e.g. 14.5:") #ask user for input
print("The square root of", myinput, "is approx." , sqrt(myinput))

"""


def sqrt(myinput):

    float(myinput) #convert input from string to a float, as want to initially make it possible for input to accept int or float input

    r = myinput
    precision = 10 ** (-10)
    calc = 1
    
    while abs(myinput - r * r) > precision:
        calc += 1
        print("calculating", calc)
        r = (r + myinput / r) / 2

    "return round(r,100) #The square root of 2 is approx. 1.4142135623746899"
    return r #The square root of 2 is approx. 1.4142135623746899

myinput = 2
print("The square root of", myinput, "is approx." , sqrt(myinput))



square_root_of2 = 1.4142135623730950488016887242096980785696718753769480731766797379907324784621 # https://apod.nasa.gov/htmltest/gifcity/sqrt2.1mil this website shows square root of 2 to million



