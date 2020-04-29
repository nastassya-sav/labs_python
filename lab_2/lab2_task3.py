import sys
import os


def msort(x): # sorts words in a line
    result = []
    if len(x) < 2:
        return x
    print(len(x))
    left = msort(x[:int(len(x) / 2)])  # get the sorted left half of the array
    #print(left)
    right = msort(x[int(len(x) / 2):])  # get the sorted right half of the
    # array
    while (len(left) > 0) or (len(right) > 0):  # while at least one of the
        # arrays is not empty
        if len(left) > 0 and len(right) > 0:  # until both arrays are empty
            if len(left[0]) > len(right[0]):  # compare the first elements of
                # both arrays along the word length
                result.append(right[0]) # write the smaller one to the result
                right.pop(0)  # remove this smaller one
            else:
                result.append(left[0]) # write the smaller one to the result
                left.pop(0)  # remove this smaller one
        elif len(right) > 0:  # unless the right one is empty
            for i in right:  # go through the elements of the right array
                result.append(i)  # assign to the result all right array
                right.pop(0)
        else:
            for i in left:
                result.append(i)
                left.pop(0)
    return result


def countOfSymbols(obj): # counting characters per line
    result = 0
    for i in obj: # go through the words of the list
        result += len(i)
    return result

def msort2(x): # sorts lines
    result = []
    if len(x) < 2:
        return x
    left = msort2(x[:int(len(x) / 2)]) # the left half is taken (if there are
    # 7 elements, it will take the first 3)
    # divide the left half and so on until 1 element is left
    os.system("cls")
    print('Sorting. Wait, please..')
    right = msort2(x[int(len(x) / 2):])
    os.system("cls")
    print('Sorting. Wait, please...')
    while (len(left) > 0) or (len(right) > 0):
        if len(left) > 0 and len(right) > 0:
            if countOfSymbols(left[0]) > countOfSymbols(right[0]):  # compare
                # rows by the number of characters without a space
                result.append(right[0])
                right.pop(0)
            else:
                result.append(left[0])
                left.pop(0)
        elif len(right) > 0:
            for i in right:
                result.append(i)
                right.pop(0)
        else:
            for i in left:
                result.append(i)
                left.pop(0)
    return result

def main():
    filename = 'result'
    choose = 0  # variable responsible for the user's choice
    incorrect_input = True
    list = []
    if len(sys.argv) > 1:
        filename = sys.argv[1] # if through the command line we set the name
        # of the file in which we write the result
    while incorrect_input:
        try:
            choose = int(input('0. Input data from file\n1. '
                               'Input data from keyboard\n2. '
                               'To exit\n'))
            incorrect_input = False  # when entered int
        except ValueError:
            incorrect_input = True
            print('Input integer number, please')
        if choose != 0 and choose != 1 and choose != 2:
            print('Number must be 0 or 1 or 2')
            incorrect_input = True
    if choose == 0:
        f = open('file2.txt', 'r')
        percent = -1
        linesOfFile = f.readlines()  #list of lines of the source file
        count = len(linesOfFile)  # number of lines of the source file
        ind = 0
        for line in linesOfFile: # go through the lines of the source file
            ind += 1  # measure the current line
            if percent != ind * 100 // count: # output only when there is a
                # percentage change
                percent = ind * 100 // count  # change percentage
                os.system("cls")
                print("Percent of reading file is {p}".format(p = percent))
                # line [: line .__ len __ () - 1 - list of words in a line
                # without the last character (go to a new line),
                # divide by spaces, sorting inside a line by the length of
                # words, add to the list
            list.append(msort(line[:line.__len__() - 1].split(' ')))
    elif choose == 1:
        count = int(input('Input count of lines\n'))
        for i in range(count):
            list.append(msort(input('Input line\n').split(' '))) # breaks
            # lines by spaces and sorts by word length
    elif choose == 2:
        exit()
    list = msort2(list) # assign the list to it, but only sorted by the number
    # of characters in the string
    text = ''
    percent = -1 # percentages are displayed when there is a difference
    # between them,
    # respectively, if we enter 0, but there will be equality
    for i in range(len(list)): # go from 0 to the number of lines-1,
        # len (list) - number of lines
        if percent != (i + 1) * 100 // len(list):
            percent = (i + 1) * 100 // len(list)
            os.system("cls")
            print("Percent of writing file is {p}".format(p=percent))
        for word in list[i]: # go through the words in each line,
            # list [i] -i-th line
            text += ''.join(word) + ' ' # lead to str, assign the words
            # separated by spaces to the result
        text += '\n'
    my_file = open(filename + '.txt', 'w')
    my_file.write(text)
    my_file.close()


if __name__ == "__main__":
    main()
