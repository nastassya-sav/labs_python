import sys


def flatten_it(y):
    for x in y:
        if x == y:  #if self-referencing array
            raise ValueError
        if hasattr(x, '__iter__') and not isinstance(x, str): #if the element
            # is iterable but not a string
            yield from flatten_it(x)  #recursion
        else:
            if isinstance(x, int) or isinstance(x, float): #if the number
                yield int(x)
            else:  #if a string
                yield x


def main():
    obj = []
    if len(sys.argv) > 1:
        obj =sys.argv[1::]  # we take everything after the name of the program
        new = []
        for i in obj:
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace(",", "")
            new.append(i)
    else:
        new = [1,[2,[3,4,5]],6,[7,8],9,[10,[11,12,[13,[14,15]]]]]
        new[0] = new  #condition of self-referencing array
    try:
        u = []  #we write the result into it
        for i in flatten_it(new):
           u.append(i)
        print(u)
    except ValueError:
        print('Array that refers to itself')


main()