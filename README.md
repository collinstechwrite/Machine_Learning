# Machine_Learning

## Sqrt2

Last Semester we worked on Newton's method of finding square roots

[https://github.com/g00387822/pands-problem-sheet/blob/master/5-squareroot.py](https://github.com/g00387822/pands-problem-sheet/blob/master/5-squareroot.py)

I tried to reuse the code from last Semester to find the Square Root of 2

Unfortunately Python has its limitations on the amount of Decimal places that it will show [read more](https://docs.python.org/3.4/tutorial/floatingpoint.html)

After much research and frustration, I consolidated what I had learned and drafted in code



, and asked the question on StackOverFlow

### Is there a way to create more decimal points on Python without importing a library/module?

[Is there a way to create more decimal points on Python without importing a library/module?](https://stackoverflow.com/questions/64278117/is-there-a-way-to-create-more-decimal-points-on-python-without-importing-a-libra)

On Stackoverflow I received this solution to be able to complete the task



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

Gives:

1.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727


Compare with my solution below


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








I have provided references to the code of others, and have worked towards consolidating the code into one function sqrt2


The Square Root of Two to 1 Million Digits can be found on this link
[https://apod.nasa.gov/htmltest/gifcity/sqrt2.1mil](https://apod.nasa.gov/htmltest/gifcity/sqrt2.1mil)


The typical way of solving this question on Python 3 would be to do this

>>> import decimal
>>> decimal.getcontext().prec=101
>>> Decimal("2").sqrt()
Decimal('1.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727')
