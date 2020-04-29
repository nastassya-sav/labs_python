def objectToJSON(obj):
    result = ''
    if obj is None:
        return "null"
    elif type(obj) == list or type(obj) == tuple:
        result += '['  # start with a square bracket
        for i in range(obj.__len__()):  # go through the list or tuple
            # elements
            result += objectToJSON(obj[i])  # we attribute to the result
            # that the function applied to these elements will return
            if i < obj.__len__() - 1:  # need not to put an extra comma at
                # the end, obj .__ len __ () - 1 position of the last element
                result += ', '
        result += ']'
    elif type(obj) == dict:
        result += '{'
        count = 0  # needed to find out when the last element will be, so as
        # not to put a comma after it
        for key, value in obj.items():  # go through the elements of the
            # dictionary
            result += '"' + key + '": ' + objectToJSON(value)  # led the value
            # to json, because it can be anything
            if count < obj.__len__() - 1:  # need not to put an extra comma at
                # the end, obj .__ len __ () - 1 position of the last element
                result += ', '
            count += 1
        result += '}'
    elif type(obj) == int or type(obj) == float:
        return str(obj)
    elif type(obj) == str:
        return '"' + obj + '"'
    elif type(obj) == bool:
        return str(obj).lower()
    else:
        raise ValueError
    return result


def main():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "array": [1, 1.25, True, "fdsfdsfsd"],
        "dictionary": {
            "first": 25,
            "second": 'some text',
            "third": ['new text', 56, False],
            "fourth": (True, 67, [98, 54, 'hfsdjkhfkds', {
                "firstElement": 'frst',
                "secondElement": 2222,
                "thirdElement": [45, 'text', (45, 78.95, False, 'fjhdskf')]
            }]),
        },
        "zero": None
    }
    incorrect_input = True
    choose = 0
    while incorrect_input:
        try:
            choose = int(input('0. Print data in file\n1. '
                               'Print data in console\n2.'
                               'To exit\n'))
            incorrect_input = False
        except ValueError:
            incorrect_input = True
            print('Input integer number, please')
        if choose != 0 and choose != 1 and choose != 2:
            print('Number must be 0 or 1 or 2')
            incorrect_input = True
    if choose == 0:
        f = open('result.txt', 'w')
        f.write(objectToJSON(x))
        f.close()
    elif choose == 1:
        print(objectToJSON(x))
    else:
        exit()


if __name__ == "__main__":
    main()
