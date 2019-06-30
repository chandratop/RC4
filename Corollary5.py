
# Corollary :
# # Once a value of j gets repeated in three consecutive rounds (r, r +1 and r +2),
# # no value can immediately be repeated in subsequent two rounds (for N > 2).
# # In other words, if jr = jr+1 = jr+2 it is not possible to have jr+3 = jr+4.


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


def check1(j_seq):
    '''
    In the sequence of j's if j(r) = j(r+1) = j(r+2),
    then return True, else, return False.
    r is the index.
        {param} j_seq : Five consecutive values of j in a list
                        (Only first 3 used)
    '''

    return j_seq[0] == j_seq[1] == j_seq[2]

def check2(j_seq):
    '''
    If jr+3 = jr+4 then it returns False,
    if not then it returns True.
        {param} j_seq : Five consecutive values of j in a list
                        (4th and 5th values used)
    
    '''

    return not (j_seq[3] == j_seq[4])


# * Main

theorem = True

# Asks how many shuffles it needs to so the algorithm on
number_of_shuffles = int(input("How many shuffles should it check : "))

# Asks how many rounds to do for each shuffle
# -2 since we do 2 rounds to create the initial j_sequence [line 46-50]
number_of_rounds = int(input("How many times should each shuffle run : ")) - 4

while number_of_shuffles > 0 and theorem is True:

    # Initial values
    arr = [x for x in range(16)]
    shuffle(arr)
    i, j = 0, 0

    j_sequence = [j]

    # Pre-running for 4 more times to set
    # j_sequence with first five values of j
    for run in range(4):
        arr, i, j = nextarr(arr, i, j)
        j_sequence.append(j)

    # To check if the Corollary is wrong at the start itself
    if check1(j_sequence) is True:
        if check2(j_sequence) is False:
            print("Corollary 3 is wrong")
            break

    for round in range(number_of_rounds):

        # get next
        arr, i, j = nextarr(arr, i, j)

        # update j_sequence
        j_sequence[0] = j_sequence[1]
        j_sequence[1] = j_sequence[2]
        j_sequence[2] = j_sequence[3]
        j_sequence[3] = j_sequence[4]
        j_sequence[4] = j

        # To check if the Corollary is wrong
        if check1(j_sequence) is True:
            if check2(j_sequence) is False:
                print("Corollary 3 is wrong")
                break

    number_of_shuffles -= 1

if theorem is True:
    print("Corollary hasn't been proved False")
