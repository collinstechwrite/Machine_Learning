


def sqrt(my_number):


    a_index = 200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

    the_index = int(a_index)
    the_index_plus_one = int(the_index + 1)
    the_index_minus_one = int(the_index - 1)
    
    my_number_times_itself = int(my_number) * int(my_number)

    
    print("my number * my number", my_number, " * ", my_number," = \n", "        ", my_number_times_itself)
    
    
    print("index    ", the_index)
    print("index + 1", the_index_plus_one)
    print("index - 1", the_index_minus_one)
    
    if int(my_number_times_itself) == int(the_index) or int(my_number_times_itself) == int(the_index_plus_one) or int(my_number_times_itself) == int(the_index_minus_one):
        print("My number multiplied by itself now equals a number close to the index position")
        print(my_number)


    
    #Multiplies 2 by * 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    elif my_number <= 2:
        print("my number is less than or equal to 2")
        my_new_number = my_number * 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        print("returning", my_new_number)
        return sqrt(int(my_new_number))

    #greater than or equal
    elif my_number >= 200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
        print(my_number)
        return sqrt(int(my_number/2))

    #less than or equal
    elif my_number <= 200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 and my_number >2:
        print(my_number)
        return sqrt(int(my_number/2))



print(sqrt(2))

