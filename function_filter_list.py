def function_filter_list(input_list,condition):
    """
    Exercise 03 - This funtion will take up a list and an argument as a condition to be met.
    The user can then select which items are gonna be displayed or filtered based on the condition
    """
    return [item for item in input_list if item <= condition] # will return a list, but will check every item in the initial input against the threshold.