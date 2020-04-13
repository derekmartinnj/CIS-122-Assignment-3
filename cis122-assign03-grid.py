'''
Author: Derek Martin
Credit: CIS 122
Description: Create a grid based on a given integer value
'''

# Question 2
def draw_grid(integer):
    '''
    creates a grid based on 'integer' input

    Prints a grid including numbers from 1 up to the 'integer' value, repeats 'integer' number of times

    Args:
        integer (int): The int to base the grid off of

    Returns:
        None
    '''
    for i in range(integer):
        for i in range(int(integer)):
            print ((i + 1), end=" ")
        print()

# Test      
draw_grid(3)
draw_grid(5)
draw_grid(7)
