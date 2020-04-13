'''
Author: Derek Martin
Credit: CIS 122
Description: Create a fruitful function that reverses a string and returns the original and reversed strings
References: https://stackoverflow.com/questions/7961499/best-way-to-loop-over-a-python-string-backwards
'''

# Question 1
def reverse(x):
    '''
    reverses the input (a string) and returns the reversed string

    Prints out the original string then the reversed string underneath it

    Args:
        x (string): The original string to be reversed

    Returns:
        Original and reversed string
    '''
    reverse = ""
    for i in reversed(x):
        reverse = reverse + i
    return print("Original:", x), print("Returns: " + reverse)

# Test
reverse("When in the Course of human events")
