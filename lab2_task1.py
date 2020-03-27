import math


def main():

    incorrect_input = True  # variable responsible for the correctness
    # of the entered data
    choose = 0  # variable responsible for the user's choice

    while incorrect_input:
        try:
            choose = int(input('0. Input data from file\n1. '
                               'Input data from keyboard\n2.'
                               'To exit\n'))
            incorrect_input = False  # when entered int
        except ValueError:
            incorrect_input = True
            print('Input integer number, please')
        if choose != 0 and choose != 1 and choose != 2:
            print('Number must be 0 or 1')
            incorrect_input = True

    arr = []
    if choose == 1:  # enter data from the keyboard
        incorrect_input = True
        while incorrect_input:
            try:
                n = int(input('Input size of array (has to be positive): '))
                arr = [int(input('Input integer number ')) for i in range(n)]
                incorrect_input = False
                if n <= 0:
                    incorrect_input = True
            except ValueError:
                incorrect_input = True
                print('Mistake. Input integer numbers, please')
    elif choose == 2:
        exit()
    else:  # data from file
        f = open('lab_1.txt', 'r')  # open the text file in read mode
        for line in f:  # go through the lines
            array_with_numbers = line.split()  # splits a line into numbers
            # according to spaces
            for i in range(array_with_numbers.__len__()):
                arr.append(int(array_with_numbers[i]))  # add numbers
                # to the array one at a time
        f.close()
    n = arr.__len__()
    print(arr)
    length = math.ceil(math.sqrt(n))  # block length
    count = n // length  # number of blocks, integer division
    if count * length != n:  # if the array is not perfectly divided
        # into blocks
        count += 1  # add a defective block

    arr_sum = []  # array of sums
    temp_sum = 0
    for i in range(n):
        temp_sum += arr[i]
        if i % length == length - 1:  # check whether the block is over
            arr_sum.append(temp_sum)  # add the current sum
            # to the array of amounts
            temp_sum = 0  # zero the current amount to check the next block
        elif i == n - 1:  # if not the end of the block, but the last
            # element of the array
            arr_sum.append(temp_sum)  # add the sum of the defective block
            # to the array
            print(arr_sum)
    incorrect_input = True
    while incorrect_input:
        try:
            left = int(input('Input left bound ')) - 1  # (-1), because
            # indexing from 0
            right = int(input('Input right bound ')) - 1
            incorrect_input = False  # when entered int
            if left < 0 or right < 0 or left >= n or right >= n:
                incorrect_input = True
                print('Input numbers between 1 and array size')
            if left > right:  # if you mixed up the right and left borders
                left, right = right, left
        except ValueError:
            incorrect_input = True
            print('Mistake. Input integer numbers, please')
    block_left = left // length  # block number for the left border
    block_right = right // length  # block number for the right border
    result = 0
    if block_right - block_left < 2:  # when there are no blocks between them
        for k in range(left, right + 1): # range does not include upper bound
            result += arr[k]
    else:
        # summarize from the next block,
        # not forgetting that the upper bound isn't included
        # if there are blocks between them, then summarize
        for k in range(block_left + 1, block_right):
            result += arr_sum[k]
        # (block_left + 1) * length - position of the first element
        # of the next block(is not included)-
        # count remaining parts
        for k in range(left, (block_left + 1) * length):  # left remaining part
            result += arr[k]
        for k in range(block_right * length, right + 1):  # right remaining part
            result += arr[k]

    print(result)


if __name__ == "__main__":
    main()
