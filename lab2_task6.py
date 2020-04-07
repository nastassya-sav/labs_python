# в формате json список и кортеж одно и то же
# на листике-схемка с ch

def json_to_obj(s):
    if s[0] == '{':  # если фигурная скобка, то это словарь
        result = {}
        startElement = 1 # нужен, чтобы запоминать начало для элемента разбиения
        insideFirstBreakets = -1  # проверить находимся ли мы в квадратных скобках
        insideSecondBreakets = -1
        insideWord = -1
        temp = []
        for ch in range(1, s.__len__() - 1):  # прохожимся по содержимому внутри фигурных скобок( скобки игнорируем)
            if s[ch] == '"':  # если ", то или воши в слово, или вышли из него
                insideWord *= -1  # (-1)-False(вне слова), 1-True(внутри слова)
            elif (s[ch] == '[' or s[ch] == ']') and insideWord == -1:  # если попали на начало/конец списка/кортежа , insideWord == -1 (чтобы "ab[dc" не было)(список/rjhnt;)
                insideFirstBreakets *= -1  # (-1)-False(вне скобок), 1-True(внутри скобок)
            elif (s[ch] == '{' or s[ch] == '}') and insideWord == -1:    # если попали на начало/конец списка/кортежа , insideWord == -1 (чтобы "ab{dc" не было)(cловарь)
                insideSecondBreakets *= -1  # (-1)-False(вне скобок), 1-True(внутри скобок)
            if s[ch] == ',' and insideWord == -1 and insideFirstBreakets == -1 and insideSecondBreakets == -1:
                # если мы попали на запятую, не находясь при этом в слове/списке/кортеже/словаре
                temp.append(s[startElement:ch])  # в массив temp добавляем текст, содержащий ключ с его значением
                startElement = ch + 2 # чтобы не считать сам пробел и запятую
            if ch == s.__len__() - 2:  # если добрались до конца последнего слова(s.__len__() - 2 - последний элементр внутри скобок)
                temp.append(s[startElement:ch + 1])  # добавляем последнюю пару пару ключ:значение
        for k in temp:  # проходимся по парам ключ:значение
            key, value = k.split(':')  # отделяем по двоеточию
            result[key[1:key.__len__() - 1]] = json_to_obj(value[1:value.__len__()])  #key[1:key.__len__() - 1] -ключ без кавычек, добавляем в качестве значение обьект, переведенный из формата json
        return result
    elif s[0] == '[': #список/кортеж
        result = []
        insideWord = -1
        insideFirstBreakets = -1
        insideSecondBreakets = -1
        startElement = 1
        for ch in range(1, s.__len__() - 1):
            if insideWord == -1 and insideFirstBreakets == -1 and insideSecondBreakets == -1 and s[ch] == ',':
                # если мы попали на запятую, не находясь при этом в слове/списке/кортеже/словаре
                result.append(json_to_obj(s[startElement:ch])) # добавляем в список обьект, переведенный из json, ch-запятая(ее не берем)
                startElement = ch + 1 #без пробелов
            if ch == s.__len__() - 2:
                result.append(json_to_obj(s[startElement:ch + 1]))
            if s[ch] == '"':
                insideWord *= -1
            elif (s[ch] == '[' or s[ch] == ']') and insideWord == -1:
                insideFirstBreakets *= -1
            elif (s[ch] == '{' or s[ch] == '}') and insideWord == -1:
                insideSecondBreakets *= -1
        return result
    elif s[0] == '"':  # если ", то у нас просто слово
        return s[1:s.__len__() - 1]  # возвращаем слово без кавычек
    elif s == 'true':
        return True
    elif s == 'false':
        return False
    elif s == 'null':
        return None
    elif s.__contains__('.'):  # если ., то float
        return float(s)
    else:
        return int(s)  #иначе целое число


def main():
    incorrect_input = True
    choose = 0
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
    # print(obj['ndsjk'][1])


if __name__ == "__main__":
    main()