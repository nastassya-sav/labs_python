#вес файла включает в себя не только его содержимое, а еще вес даты, названия, метаданных и прочего
import random

def main():
    alphavite = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    fileName = input('Input file name\n')
    Mb = int(input('Input text file size in megabytes\n'))
    Bytes = Mb * 1048576
    K = tuple(input('Input number of words in line\n').split(','))  #интервал, сиволизирующий количество слов в строке, разбиваем по запятым
    L = tuple(input('Input length of word\n').split(','))  #интервал, сиволизирующий длину слов в строке, разбиваем по запятым

    my_file = open(fileName + '.txt', 'w') #открытие файла, если файла нет-автоматически создаст
    result = '' #строка, которую запишем в файл в конце
    while result.__sizeof__() <= Bytes:
        countOfWords = random.randint(int(K[0]), int(K[1])) # случайно генерируем количество слов в строке
        for currentWord in range(countOfWords): #создаем слова через пробел
            lengthOfWord = random.randint(int(L[0]), int(L[1])) # случайно генерируем длину слова
            word = ''.join([alphavite[random.randint(0, 51)] for i in range(lengthOfWord)]) #случайная генерация слова длины lengthOfWord, массив симовлов приводим к типу строки
            if result.__sizeof__() + word.__sizeof__() <= Bytes:
                result += word + " "
            else: #если место в файле кончилось
                break
        result += '\n'
    my_file.write(result)
    my_file.close()

if __name__ == "__main__":
    main()