
# Corollary :
# # In two consecutive rounds (r and r+1),
# # if the value of j remains constant,
# # (i.e., jr = jr+1) then Sr+1[jr+1] must be 0.


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
    In the sequence of j's if j(r) = j(r+1),
    then return True, else, return False.
    r is the index.
        {param} j_seq : Four consecutive values of j in a list
    '''

    return j_seq[0] == j_seq[1]

def check2(S_seq, j):
    '''
    If S(r+1)[jr+1] = 0, it returns True,
    else it returns False.
    r is the index.
        {param} S_seq : Sequence of arr in past two iterations
        {param} j : j(r+1)
    '''

    return S_seq[1][j] == 0


# * Main

corollary = True

# Asks how many shuffles it needs to so the algorithm on
number_of_shuffles = int(input("How many shuffles should it check : "))

# Asks how many rounds to do for each shuffle
# -1 since we do 1 round to create the initial j_sequence [line 46-50]
number_of_rounds = int(input("How many times should each shuffle run : ")) - 1

while number_of_shuffles > 0 and corollary is True:

    # Initial values
    arr = [x for x in range(16)]
    shuffle(arr)
    i, j = 0, 0

    j_sequence = [j]
    S_sequence = [arr]

    # Pre-running for 1 more time to set
    # j_sequence with first two values of j and
    # S_sequence with first two values of arr
    for run in range(1):
        arr, i, j = nextarr(arr, i, j)
        j_sequence.append(j)
        S_sequence.append(arr)

    # To check if the Corollary is wrong at the start itself
    # even though the j_sequence test is passed (check1)
    if check1(j_sequence) is True:
        if check2(S_sequence, j_sequence[1]) is False:
            print("Corollary 4 is wrong")
            break

    for round in range(number_of_rounds):

        # get next
        arr, i, j = nextarr(arr, i, j)

        # update j_sequence and S_sequence
        j_sequence[0], S_sequence[0] = j_sequence[1], S_sequence[1]
        j_sequence[1], S_sequence[1] = j, arr

        # To check if the Corollary is wrong
        # even though the j_sequence test is passed (check1)
        if check1(j_sequence) is True:
            if check2(S_sequence, j_sequence[1]) is False:
                print("Corollary 4 is wrong")
                break

    number_of_shuffles -= 1

if corollary is True:
    print("Corollary hasn't been proved False")
