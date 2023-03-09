def multiSum(num1, num2):  # this is where a function is declared
    if num1 * num2 <= 1000:  #on this line a condition was used
        return num1 * num2    # this is where a loop is used

    else:
        return num1+num2

    
hope = multiSum(32, 2)
print(hope)