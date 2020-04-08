import sys  # import the library for working with command line arguments


def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return a
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


def main():
    inp = 0
    in_correct_input = True
    while inp != 'exit':
        inp = input("Enter natural number, "
                    "or arg to be displayed in Leonardo's or exit to exit: ")
        if inp == 'exit':
            break
        else:
            try:
                if inp == 'arg':
                    if len(sys.argv) > 1:  # if there is an argument after the name
                        # of the program
                        n = int(sys.argv[1])  # trying to convert to an integer type
                        in_correct_input = False  # when entered int
                    else:
                        in_correct_input = True
                else:
                    n = int(inp)
                    in_correct_input = False  # when entered int
                if n < 0:
                    in_correct_input = True
                elif n == 0:
                    in_correct_input = True
            except ValueError:
                in_correct_input = True
                print('Input integer number, please')

            if in_correct_input == 0:
                print("Fibonacci {n}\'th number is {fib}".format(n=n,
                                                                 fib=fibonacci(n)))
                print("Leonardo {y}\'th number is {leo}".format(y=n, leo=
                (2 * fibonacci(n + 1) - 1)))


if __name__ == "__main__":
    main()