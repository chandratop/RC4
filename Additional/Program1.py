
'''
This program tests out the number of times j
occurs in the execution of the algorithm
'''


# Modules imported

from random import shuffle
from matplotlib import pyplot as plt


# Functions

def nextarr(arr, i, j, N=16):
    '''
    This function used the RC4 algorithm to
    create the next iteration of the array
    based on the values of i and j.
        {param} arr : The previous array
        {param} i : The previous i
        {param} j : The previous j
        {param} N : Default parameter 16, for array length
    '''

    # algorithm
    i = (i + 1) % N
    j = (j + arr[i]) % N

    # swap
    arr[i], arr[j] = arr[j], arr[i]

    # return requires tuple unpacking
    return arr, i, j

N - int(input())