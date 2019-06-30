
# Corollary :
# # During RC4 PRGA, there cannot be a continuously increasing sequence of j
# # of length more than 3 or in other words there cannot exist any r for which
# # (jr+1 −jr) = (jr+2 −jr+1) = (jr+3 −jr+2) = k where (k > 1).


# * Modules imported

from random import shuffle


# * Functions

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


def check(j_seq):
    '''
    If four consecutive values in the sequence of j
    are decreasing by the same number then return False and that number.
    Otherwise return True (for Theorem OK) and None
    But that number has to be more than 1
        {param} j_seq : Four consecutive values of j in a list
    '''
    
    difference = None
    condition = j_seq[1] - j_seq[0] == j_seq[2] - j_seq[1] == j_seq[3] - j_seq[2]
    if condition is True and difference > 1:
        difference = j_seq[1] - j_seq[0]
    else:
        condition, difference = False, None

    return not(condition), difference


# * Main

corollary = True
N = 16

# Asks how many shuffles it needs to so the algorithm on
number_of_shuffles = int(input("How many shuffles should it check : "))

# Asks how many rounds to do for each shuffle
# -3 since we do 3 rounds to create the initial j_sequence [line 46-50]
number_of_rounds = int(input("How many times should each shuffle run : ")) - 3

while number_of_shuffles > 0 and corollary is True:

    # Initial values
    arr = [x for x in range(N)]
    shuffle(arr)
    i, j = 0, 0

    j_sequence = [j]

    # Pre-running for 3 more times to set
    # j_sequence with first four values of j
    for run in range(3):
        arr, i, j = nextarr(arr, i, j)
        j_sequence.append(j)

    # To check if the Corollary is wrong at the start itself
    checker, difference = check(j_sequence)
    if checker is False:
        print("Corollary 6 is wrong and difference is ", difference)

    for round in range(number_of_rounds):

        # get next
        arr, i, j = nextarr(arr, i, j)

        # update j_sequence
        j_sequence[0] = j_sequence[1]
        j_sequence[1] = j_sequence[2]
        j_sequence[2] = j_sequence[3]
        j_sequence[3] = j

        # To check if the Corollary is wrong
        checker, difference = check(j_sequence)
        if checker is False:
            print("Corollary 6 is wrong and difference is ", difference)

    number_of_shuffles -= 1

if corollary is True:
    print("Corollary hasn't been proved False")
