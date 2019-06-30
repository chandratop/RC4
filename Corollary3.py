
# Corollary :
# # If (jr = jr+1 = jr+2) then,
# # ir+2 = jr+2 and
# # Sr+1[jr+1] = Sr+2[ir+2] = Sr+2[jr+2] = 0


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
        {param} j_seq : Three consecutive values of j in a list
    '''

    return j_seq[0] == j_seq[1] == j_seq[2]

def check2(i, j):
    '''
    If i(r+2) = j(r+2) it returns True,
    else it returns False.
    r is the index.
        {param} i : i(r+2)
        {param} j : j(r+2)
    '''

    return i == j

def check3(S_seq, i, j_seq):
    '''
    If  Sr+1[jr+1] = Sr+2[ir+2] = Sr+2[jr+2] = 0 then,
    it returns True, else it returns False.
    r is the index.
        {param} S_seq : Contains the last two iterations of arr
        {param} i : i(r+2)
        {param} j_seq : Used to take j(r+1) and j(r+2) values
    '''

    return S_seq[1][j_seq[1]] == S_seq[2][i] == S_seq[2][j_seq[2]] == 0


# * Main

corollary = True
N = 16

# Asks how many shuffles it needs to so the algorithm on
number_of_shuffles = int(input("How many shuffles should it check : "))

# Asks how many rounds to do for each shuffle
# -2 since we do 2 rounds to create the initial j_sequence [line 46-50]
number_of_rounds = int(input("How many times should each shuffle run : ")) - 2

while number_of_shuffles > 0 and corollary is True:

    # Initial values
    arr = [x for x in range(N)]
    shuffle(arr)
    i, j = 0, 0

    j_sequence = [j]
    S_sequence = [arr]
    i_2 = i # i(r+2)

    # Pre-running for 2 more times to set
    # j_sequence with first three values of j and
    # S_sequence with first three values of arr
    for run in range(2):
        arr, i, j = nextarr(arr, i, j)
        j_sequence.append(j)
        S_sequence.append(arr)
        i_2 = i

    # To check if the Corollary is wrong at the start itself
    # even though the j_sequence test is passed (check1)
    if check1(j_sequence) is True:
        if check2(i_2, j_sequence[2]) and check3(S_sequence, i_2, j_sequence) is False:
            print("Corollary 3 is wrong")
            break

    for round in range(number_of_rounds):

        # get next
        arr, i, j = nextarr(arr, i, j)

        # update j_sequence and S_sequence
        j_sequence[0], S_sequence[0] = j_sequence[1], S_sequence[1]
        j_sequence[1], S_sequence[1] = j_sequence[2], S_sequence[2]
        j_sequence[2], S_sequence[2] = j, arr

        # To check if the Corollary is wrong
        # even though the j_sequence test is passed (check1)
        if check1(j_sequence) is True:
            if check2(i_2, j_sequence[2]) and check3(S_sequence, i_2, j_sequence) is False:
                print("Corollary 3 is wrong")
                break

    number_of_shuffles -= 1

if corollary is True:
    print("Corollary hasn't been proved False")
