def recursive_inner_plus(input_list):
    """
    Exercise 02 - Finding the inner most numbers, 
    so that we can add 1 to each one of them, and finally 
    resulting in a list with the answer. Recursion is used.
    """
    for item in input_list:
        if isinstance(item,list): #to check if the input is from a specific class, a list in this case
            return recursive_inner_plus(item) #will use recursive, or check the items again and again until there's no other list left

    #The inner most list is found, we then need to calculate the n+1 for each element.

    return [element +1 for element in input_list] #now it will add 1 to the list, resulting in a list