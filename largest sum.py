"""
Take an array with positive and negative integers and find the maximum sum of that array
"""

def largest(arr):
    # make sure array is of appropriate length
    if len(arr) == 0:
        return print('Too small')

    # assigning the first element in the array to both variables
    max_sum = current_sum = arr[0] 

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return print(max_sum)

largest([7, 1, 2, -1, 3, 4, 10, -12, 3, 21, -19])