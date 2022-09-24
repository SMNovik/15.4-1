def changeText(text):
    """
    Функция принимает строку с текстом.
    Убирает все знаки препинания и возвращает
    список, состоящий из слов текста.
    """
    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        text = text.replace(i, '')

    return text.split()

def mostCommon(text, length=0):
    """
    Функция принимает список и ограничение по длине.
    Возвращает самый часто встречающийся элемент.
    Если есть несколько элементов с одинаковой самой большой частотой, то вернёт их все.
    """
    most_common = []      # список слов чаще всего встречаемыхв тексте
    qty_most_common = 0   # сколько раз встречается слово в тексте

    for item in text:
        if len(item) > length:
            qty = text.count(item)  # счетчик сколько раз встречается слово в тексте
            if qty > qty_most_common and qty > 2:
                qty_most_common = qty  # присвается новое значение счетчику количества
                most_common = [item]
            elif qty == qty_most_common:
                most_common.append(item)

    return list(set(most_common))

def mostLength(text):
    """
    Функция принимает список.
    Возвращает самый длинный элемент.
    Если есть несколько элементов с одинаковой самой большой длиной, то вернёт их все.
    """
    most_length = []
    qty_most_length = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for item in text:
        for char in item:
            if char not in alphabet:
                charEn = False
            else:
                charEn = True

        if charEn:
            qty = len(item)
            if qty > qty_most_length:
                qty_most_length = qty
                most_length = [item]
            elif qty == qty_most_length:
                most_length.append(item)

    return list(set(most_length))

# nameFile = input('Название файла: ')
nameFile = r'F:\ОБУЧЕНИЕ ATI\курс QA\модуль 15\yesterday.txt'
with open(nameFile, encoding='utf-8-sig') as f:
    fileText = f.read()

fileText = changeText(fileText)
print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 2)}')
print(f'Список самых длинных английских слов: {mostLength(fileText)}')