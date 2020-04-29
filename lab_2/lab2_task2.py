import random
import sys
import os


def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Mb = 0
    incorrectInput = True
    if len(sys.argv) >= 5: # if you entered all the necessary arguments
        fileName = sys.argv[1]
        try:
            Mb = int(sys.argv[2])
            if Mb <= 0:
                Mb = 0
            else:
                incorrectInput = False
        except ValueError: # when you entered mb not int
            pass
    else:
        fileName = input('Input file name or 0 to exit\n')
    if fileName == '0':
        exit()
    while incorrectInput:
        try:
            Mb = int(input('Input text file size in megabytes\n'))
            incorrectInput = False
            if Mb <= 0:
                incorrectInput = True
        except ValueError: # when you entered mb not int
            pass
    Bytes = Mb * 1048576

    # interval, symbolizing the number of words in a line, divided by commas
    if len(sys.argv) >= 5:
        K = tuple(sys.argv[3].split(','))
    else:
        K = tuple(input('Input number of words in line\n').split(','))
    try:
        if K.__len__() >= 2:  # checking that we entered 2 numbers, if more
            # than 2 then it will ignore
            K = (int(K[0]), int(K[1]))
            if K[0] < 0 or K[1] < 0:
                K = (10, 100)
            if K[0] > K[1]:
                K = (K[1], K[0])
        else: # if nothing is entered or one
            K = (10, 100)
    except ValueError: # if at least one of the first two numbers is not
        # an integer
        K = (10, 100)

    # interval, symbolizing the length of words in a line, divided by commas
    if len(sys.argv) >= 5:
        L = tuple(sys.argv[4].split(','))
    else:
        L = tuple(input('Input length of word\n').split(','))
    try:
        if L.__len__() >= 2:
            L = (int(L[0]), int(L[1]))
            if L[0] < 0 or L[1] < 0:
                L = (3, 10)
            if L[0] > L[1]:
                L = (L[1], L[0])
        else:
            L = (3, 10)
    except ValueError:
        L = (3, 10)

    my_file = open(fileName + '.txt', 'w')  # opening a file if there is no
    # file will automatically create
    result = '' # line that will be written to the file at the end
    percents = -1
    while result.__sizeof__() <= Bytes:
        countOfWords = random.randint(K[0], K[1]) # randomly generate the
        # number of words per line
        for currentWord in range(countOfWords):
            lengthOfWord = random.randint(int(L[0]), int(L[1])) # randomly
            # generate word length
            word = ''.join([alphabet[random.randint(0, 51)] for i
                            in range(lengthOfWord)]) # random generation of a
            # word of length lengthOfWord, an array of characters is cast to a
            # string type
            if result.__sizeof__() + word.__sizeof__() <= Bytes:
                result += word + " "
                currentPercent = result.__sizeof__() * 100 // Bytes
                if currentPercent != percents:  # if the current percentage is
                    # different from the previous
                    percents = currentPercent
                    os.system("cls") # console cleaning
                    print("Percent of program executing is"
                          " {p}%".format(p = percents))
            else: # if the place in the file runs out
                break
        result += '\n'
    my_file.write(result)
    my_file.close()


if __name__ == "__main__":
    main()
