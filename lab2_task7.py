import sys #импортируем библитеку для работы с аргументами командной строки

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

def main():
    n = 0
    inCorrectInput = True

    if len(sys.argv) > 1:#если есть аргумент после названия проги
        try:
            n = int(sys.argv[1])#пытаемся преобразовать к целому тbпу
            inCorrectInput = False  # когда ввели int
            if n < 0:
                inCorrectInput = True
        except ValueError:
            inCorrectInput = True

    if inCorrectInput:  #либо нет аргумента командной строки, либо он
                        # неверного формата
        while inCorrectInput:
            try:
                n = int(input("int n: "))
                inCorrectInput = False  # когда ввели int
                if n < 0:
                    inCorrectInput = True
            except ValueError:
                inCorrectInput = True
                print('Input integer number, please')

    print("Fibonacci {n}\'th number is {fib}".format(n = n,
                                                     fib = fibonacci(n)))
    print("Leonardo {y}\'th number is {leo}".format(y = n,
                                                    leo =
                                                    (2*fibonacci(n+1)-1)))

if __name__ == "__main__":
  main()