"""

You know 12<2. You know 22>2. So 1<2–√<2 so its first decimal digit is 1.

You check 1.52>2. You check 1.252<2. You check 1.3752<2. You check 1.43752>2. You check 1.406252<2.

Now you know 1.40625<2–√<1.4375 so you know the first two digits are 1.4.

"""


""" So, 9>7 is read as '9 is greater than 7'."""




find_square_root = 2
try_variable = 1
try_variable_incrementer = 0.1
myrounder = 1


"""while 2 > 1 ** 1:                                                  ( while 2 is more than 1**1 squared)"""

while find_square_root > try_variable ** try_variable:
    print(try_variable ** try_variable)
    print(find_square_root, "is greater than ", try_variable, "squared")
    try_variable = round(try_variable + try_variable_incrementer,myrounder)
    myrounder += 1
    
while find_square_root > try_variable ** try_variable:
    print(try_variable ** try_variable)
    print(find_square_root, "is greater than ", try_variable, "squared")
    try_variable = round(try_variable + try_variable_incrementer,myrounder)
    myrounder += 1    


for seq in range(50,1000,100):
    print(seq)

a = 1.0000000000000000000000000000000000000000000000000000000000000000000000000000001

b = a + a

print (str(a))
print(str(b))


import numpy.random 
print(numpy.random.__file__) 


import decimal
print(decimal.__file__) 



def decimals(number):
    dividend = 1
    while dividend:
        return dividend // number
        dividend = dividend % number * 10


print(decimals(80))




def decimals2(number):    
    """
    Takes a number and generates the digits of  1/n.

    """
    divisor = 2
    dividend = 1
    remainder = 1

    while remainder:
        #Floor division is the // operator        
        quotient = dividend // divisor
        remainder = dividend % divisor

        if remainder < divisor:
            dividend = remainder * 10
        else:
            dividend = remainder
        yield quotient

print(decimals2(89))

    
