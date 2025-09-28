def while_inner_plus(input_list):
    """
    Exercise 01 - Finding the inner most numbers, 
    so that we can add 1 to each one of them, and finally 
    resulting in a list with the answer. While loop is used.
    """
    #Create conditions so that the while loop can break
    final_list = input_list
    met_condition = True #Set it to get it running

    while met_condition:
        met_condition = False #will change to get it to stop
        #Check for the inner most list containing only integers
        for item in final_list:
            if isinstance(item,list): #to check if the input is from a specific class, a list in this case
                final_list = item
                met_condition = True
                break
    #The inner most list is found, we then need to calculate the n+1 for each element.

    result = [element +1 for element in final_list]

    return result