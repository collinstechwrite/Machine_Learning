
print(2 * 10 ** 200)


def sqrt(my_number):

    a_index = 200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

    the_index = int(a_index)
    the_index_plus_one = int(the_index + 1)
    the_index_minus_one = int(the_index - 1)
    
    my_number_times_itself = int(my_number) * int(my_number)

    if int(my_number_times_itself) == int(the_index):
        print("My number multiplied by itself now equals a number close to the index position")
        print(my_number) 
        return my_number

    #greater than
    elif int(my_number_times_itself) > int(the_index):
        print(my_number)
        return sqrt(int(my_number/2))

    #less than
    elif int(my_number_times_itself) < int(the_index):
        print(my_number)
        return sqrt(int(my_number + 1))

print(format(sqrt(200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000), ',.100f'))


"""----------------------------------------------------------------------------------------------------------------------"""







def mySqrt(x):
    x = x * 10 ** 200 #CONVERT TO A REALLY LARGE INTEGER
    r = x



    precision = 1 ** (-1)

    # WHILE X - R * R IS GREATER THAN PRECISION
    while abs(x - r * r) > precision:
        #R WILL EQUAL R PLUS X DIVIDED BY R
        r = (r + x / r) / 2

    # turn result into a string
    text = str(r)

    # insert
    text = text[:1] + "." + text[2:] 
    return r

find_square_root_of = 2
answer = format(mySqrt(find_square_root_of), '.0f')
print(answer)

"""----------------------------------------------------------------------------------------------------------------------"""





x = 2 * 10 ** 200

r = x

def test_diffs(x, r):
    d0 = abs(x - r**2)
    dm = abs(x - (r-1)**2)
    dp = abs(x - (r+1)**2)
    minimised = d0 <= dm and d0 <= dp
    below_min = dp < dm
    return minimised, below_min

while True:
    oldr = r
    r = (r + x // r) // 2

    minimised, below_min = test_diffs(x, r)
    if minimised:
        break

    if r == oldr:
        if below_min:
            r += 1
        else:
            r -= 1
        minimised, _ = test_diffs(x, r)
        if minimised:
            break

print(f'{r // 10**100}.{r % 10**100:0100d}')



"""----------------------------------------------------------------------------------------------------------------------"""




def sqrt2(my_number): # I researched how to do a nested function to encapsulate sqrt2 as the overarching function, outer / inner function see https://stackabuse.com/python-nested-functions/
                      # my_number is 2, when the function sqrt2 is called sqrt2(2), see last line of code below


    x = my_number * 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    # Because Python does not do 100 decimal places, we multiply 2 to a really large integer, where the square root of this number will be an integer length of 101 characters
    # e.g. 14142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
    # is square root of 200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    # The above could also be coded this way x = my_number * 10 ** 200
 
    r = x

    def test_diffs(x, r): 

        # test_diffs is the inner function of sqrt2, the code which I used for this inner function was given to me by expert on stackoverflow
        # https://stackoverflow.com/questions/64278117/is-there-a-way-to-create-more-decimal-points-on-python-without-importing-a-libra/64278569?noredirect=1#comment113668731_64278569
        # on my question on stackoverflow I describe the research I have done, and how far I got with a possible solution
        
        
        d0 = abs(x - r**2)
        dm = abs(x - (r-1)**2)
        dp = abs(x - (r+1)**2)
        minimised = d0 <= dm and d0 <= dp
        below_min = dp < dm
        return minimised, below_min

    while True:
        oldr = r # this is a variable used for keeping track of original numaber
        r = (r + x // r) // 2

        minimised, below_min = test_diffs(x, r)
        if minimised:
            break

        if r == oldr:
            if below_min:
                r += 1 # increment r by 1
            else:
                r -= 1 # decrease r by 1
            minimised, _ = test_diffs(x, r)

            if minimised:
                break

    # We could present answer using print formatting from original stackoverflow answer
    # https://stackoverflow.com/questions/64278117/is-there-a-way-to-create-more-decimal-points-on-python-without-importing-a-libra/64278569?noredirect=1#comment113668731_64278569
    # print(f'{r // 10**100}.{r % 10**100:0100d}')"""

    # Or we can code to convert the final number into a string, and separate the string into two parts and add a fullstop in the middle https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string
    r = str(r)
    text = r[:1] + "." + r[1:]
    print(text)




sqrt2(2) # call the function sqrt









