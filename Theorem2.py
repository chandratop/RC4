
# THEOREM :
# # During RC4 PRGA, in 3 consecutive rounds (r, r + 1 and r + 2),
# # j cannot take 3 consecutive integer values


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
    In the sequence of j's if j(r+2) = j(r+1) + 1 = j(r) + 2,
    then return False as theorem is wrong, else, return True
    r is the index
        {param} j_seq : Three consecutive values of j in a list
    '''

    return not (j_seq[2] == (j_seq[1] + 1) == (j_seq[0] + 2))


# * Main

theorem = True

# Asks how many shuffles it needs to so the algorithm on
number_of_shuffles = int(input("How many shuffles should it check : "))

# Asks how many rounds to do for each shuffle
# -2 since we do 2 rounds to create the initial j_sequence [line 46-50]
number_of_rounds = int(input("How many times should each shuffle run : ")) - 2

while number_of_shuffles > 0 and theorem is True:

    # Initial values
    arr = [x for x in range(16)]
    shuffle(arr)
    i, j = 0, 0

    j_sequence = [j]

    # Pre-running for 2 more times to set
    # j_sequence with first three values of j
    for run in range(2):
        arr, i, j = nextarr(arr, i, j)
        j_sequence.append(j)

    # To check whether the already created j_sequence
    # disproves the throrem or not
    if check(j_sequence) is False:
        print("Theorem 2 is wrong")
        break

    for round in range(number_of_rounds):

        # get next
        arr, i, j = nextarr(arr, i, j)

        # update j_sequence
        j_sequence[0] = j_sequence[1]
        j_sequence[1] = j_sequence[2]
        j_sequence[2] = j

        # To check whether the created j_sequence
        # disproves the throrem or not
        if check(j_sequence) is False:
            print("Theorem 2 is wrong")
            theorem = False
            break

    number_of_shuffles -= 1

if theorem is True:
    print("Theorem hasn't been proved False")
