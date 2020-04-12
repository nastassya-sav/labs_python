import sys  # import the library for working with command line arguments


def power_of_two(n):
    if n & (n - 1) == 0:  # use bitwise "And"
        # if n and (n-1) do not match any bit <==> n-exact power of two
        return 1
    else:
        return 0


def main():
    inp = 0
    in_correct_input = True
    if len(sys.argv) == 2 and (sys.argv[1]).isnumeric():
        n = int(sys.argv[1])
        if power_of_two(n) == 1:
            print("Yes")
        else:
            print("No")

    while inp != 'exit':
        inp = input("Enter natural number, "
                    "or arg to be displayed in power_of_two or exit "
                    "to exit: ")
        if inp == 'exit':
            break
        else:
            try:

                if len(sys.argv) > 1:  # if there is an argument after the
                    # name of the program
                    n = int(sys.argv[1])  # trying to convert to an
                    # integer type
                    in_correct_input = False  # when entered int
                else:
                    n = int(inp)
                    in_correct_input = False  # when entered int
                if n < 0:
                    in_correct_input = True
                elif n == 0:
                    in_correct_input = True
                elif n == 2:
                    exit()
            except ValueError:
                in_correct_input = True
                print('Input integer number, please')

            if in_correct_input == 0:
                if power_of_two(n) == 1:
                    print("Yes")
                else:
                    print("No")


if __name__ == "__main__":
    main()
