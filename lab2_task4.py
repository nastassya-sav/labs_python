import sys

def flatten_it(obj):
    res = []
    for it in obj: #проходимся по кажому элементу списка
        if it == obj: #если есть самоссылка -> выбрасываем исключение
            raise ValueError
        try:
            iter(it) # пытаемся получить итератор объекта, если не получается- вылетает исключение
            res += flatten_it(it) # добавляем к результату линеаризированный объект
        except TypeError:
            res.append(it) # просто добавляем к результату объект
    return res

def main():
    obj = []
    if len(sys.argv) > 1:
        obj =(sys.argv[1]) #sys.argv[1] -> список
    else:
        obj = [1,[2,[3,4,5]],6,[7,8],9,[10,[11,12,[13,[14,15]]]]]
        obj[0] = obj #самоссылающийся массив, 1 элемент массива будет ссылаться (указывает на) на этот же массив
    try:
        print(flatten_it(obj))
    except ValueError: #если самоссылающийся массив содержится в массиве
        print('Array that refers to itself')













if __name__ == "__main__":
    main()