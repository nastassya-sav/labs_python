# во время работы любых программ под них выделяется оперативная память за счет использования переменных(память под них)
# оперативная память расходуется только на ресурсы, выделяемые во время выполнения программы

import sys
import os


def msort(x): # сортирует слова в строке
    result = []
    if len(x) < 2:
        return x
    left = msort(x[:int(len(x) / 2)])
    right = msort(x[int(len(x) / 2):])
    while (len(left) > 0) or (len(right) > 0):
        if len(left) > 0 and len(right) > 0:
            if len(left[0]) > len(right[0]):
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

def countOfSymbols(obj): # подсчёт символов в строке
    result = 0
    for i in obj:
        result += len(i)
    return result

def msort2(x): # сортирует строки
    result = []
    if len(x) < 2:
        return x
    left = msort2(x[:int(len(x) / 2)]) # берется левая половина( если элементов 7, возьмет первые 3)
    # делим левую половину и так далее пока не останется 1 элемент
    os.system("cls")
    print('Sorting. Wait, please..')
    right = msort2(x[int(len(x) / 2):])
    os.system("cls")
    print('Sorting. Wait, please...')
    while (len(left) > 0) or (len(right) > 0):
        if len(left) > 0 and len(right) > 0:
            if countOfSymbols(left[0]) > countOfSymbols(right[0]):
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
        filename = sys.argv[1] #если через команденую строку задаем название файла, в который запишем результат
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
        procent = -1
        linesOfFile = f.readlines()  # список строк исходного файла
        count = len(linesOfFile)  # количество строк исходного файла
        ind = 0
        #for line in linesOfFile:  # проходимся по строкам исходного файла
        #    ind += 1  # отмеряем текущую строку
        #    if procent != ind * 100 // count:  # выводи только, когда есть изменение в процентах
        #        procent = ind * 100 // count  # меняем процент
        #        os.system("cls")
        #        print("Procent of reading file is {p}".format(p = procent))
        #    list.append(msort(line[:line.__len__() - 1].split(' '))) #line[:line.__len__() - 1 - список символов строки без последнего символа(переход на новую строку), разбиваем по пробелам, сортировка внутри строки по длине слов, добавляем в список
    elif choose == 1:
        count = int(input('Input count of lines\n'))
        for i in range(count):
            list.append(msort(input('Input line\n').split(' '))) # разбивает строки по проблелам и сортирует по длине слов
    elif choose == 2:
        exit()
    list = msort2(list) # списку присваиваем его же, но только отсортированный по количеству символов в строке
    text = ''
    procent = -1 # проценты выводятся, когда есть разница между ними, соответсвенно если введем 0, но будет равенство
    for i in range(len(list)): # от 0 до количества строк-1
        if procent != (i + 1) * 100 // len(list): #len(list)-количество строк
            procent = (i + 1) * 100 // len(list)
            os.system("cls")
            print("Procent of writing file is {p}".format(p=procent))
        for word in list[i]: # прохоимся по словам в каждой строке, list[i]-i-ая строка
            text += ''.join(word) + ' ' # приводим к str, был ['g','h','t','y']-> 'ghty',''.join(word)- наьор символов соединяет в одно слово к результату приписываем слова через пробел
        text += '\n'
    my_file = open(filename + '.txt', 'w')
    my_file.write(text)
    my_file.close()


if __name__ == "__main__":
    main()