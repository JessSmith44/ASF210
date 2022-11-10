def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

def loop1Rec(num = 0,odd_sum = 0):
    # Duplicate the loop1 function using recursion
    # if num < 20 
    #    then check if its odd,
            # return(loop1Rec(num+1, odd_sum + num))
        # otherwise
            # return(loop1Rec(num+1, odd_sum))
    # otherwise 
    #   return odd_sum
    

def loop2Rec(num = 0,even_sum = 0):
    # Duplicate the loop2 function using recursion
    # if num < 20 
    #    then check if its even,
            # return(loop1Rec(num+1, even_sum + num))
        # otherwise
            # return(loop1Rec(num+1, even_sum))
    # otherwise 
    #   return even_sum

