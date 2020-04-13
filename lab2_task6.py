def json_to_obj(s):
    if s[0] == '{':  # dictionary
        result = {}
        startElement = 1 # needed to remember the start for a split element
        insideFirstBreakets = -1  # check if we are in square brackets
        insideSecondBreakets = -1
        insideWord = -1
        temp = []
        for ch in range(1, s.__len__() - 1):  # go through the contents inside
            # curly brackets (ignore the brackets)
            if s[ch] == '"': # if ", then either entered the word or left it
                insideWord *= -1  # (-1) -False (outside the word),
                # 1-True (inside the word)
            elif (s[ch] == '[' or s[ch] == ']') and insideWord == -1:  # if at
                # the beginning / end of the list / tuple
                insideFirstBreakets *= -1  # (-1)-False (outside the
                # brackets), 1-True (inside the brackets)
            elif (s[ch] == '{' or s[ch] == '}') and insideWord == -1: # if at
                # the beginning / end of the list / tuple
                insideSecondBreakets *= -1 # (-1)-False (outside the
                # brackets), 1-True (inside the brackets)
                # if on a comma, without being in the word / list / tuple /
                # dictionary
            if s[ch] == ',' and insideWord == -1 and \
                    insideFirstBreakets == -1 and insideSecondBreakets == -1:
                temp.append(s[startElement:ch])  # add the text containing the
                # key with its value to the temp array
                startElement = ch + 2 # to not count the space and comma
            if ch == s.__len__() - 2:  # if you get to the end of the last
                # word (s .__ len __ () - 2 - the last element inside the
                # brackets)
                temp.append(s[startElement:ch + 1])  # add the last pair
                # key: value
                print(temp)
        for k in temp:  # go through the pairs key: value
            key, value = k.split(':')
            # key [1: key .__ len __ () - 1] - the key without quotes, add the
            # object translated from json format as the value
            result[key[1:key.__len__()-1 ]] = json_to_obj(
                value[1: value.__len__()])
        return result
    elif s[0] == '[': # list / tuple
        result = []
        insideWord = -1
        insideFirstBreakets = -1
        insideSecondBreakets = -1
        startElement = 1
        for ch in range(1, s.__len__() - 1):
            # if we are on a comma without being in the word / list / tuple /
            # dictionary
            if insideWord == -1 and insideFirstBreakets == -1 and\
                    insideSecondBreakets == -1 and s[ch] == ',':
                result.append(json_to_obj(s[startElement:ch])) # add the
                # object translated from json to the list,
                # ch-comma (we don’t take it)
                startElement = ch + 2
            if ch == s.__len__() - 2:
                result.append(json_to_obj(s[startElement:ch + 1]))
            if s[ch] == '"':
                insideWord *= -1
            elif (s[ch] == '[' or s[ch] == ']') and insideWord == -1:
                insideFirstBreakets *= -1
            elif (s[ch] == '{' or s[ch] == '}') and insideWord == -1:
                insideSecondBreakets *= -1
        return result
    elif s[0] == '"':  # if ", then the word
        return s[1:s.__len__() - 1]  # return the word without quotes
    elif s == 'true':
        return True
    elif s == 'false':
        return False
    elif s == 'null':
        return None
    elif s.__contains__('.'):  # if., then float
        return float(s)
    else:
        return int(s)  # else an integer


def main():
    incorrect_input = True
    choose = 0
    while incorrect_input:
        try:
            choose = int(input('0. Input data from file\n1. '
                               'Input data from keyboard\n2. '
                               'To exit\n'))
            incorrect_input = False
        except ValueError:
            incorrect_input = True
            print('Input integer number, please')
        if choose != 0 and choose != 1 and choose != 2:
            print('Number must be 0 or 1 or 2')
            incorrect_input = True
    stringInJSON = ''
    if choose == 0:
        f = open('input.txt', 'r')
        stringInJSON = f.readline()
        f.close()
    elif choose == 1:
        stringInJSON = input('Input your string in JSON\n')
    elif choose == 2:
        exit()
    obj = json_to_obj(stringInJSON)
    print(obj)

if __name__ == "__main__":
    main()