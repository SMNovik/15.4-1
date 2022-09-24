alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
name_f = input('Путь к файлу:')
# name_f = r'F:\ОБУЧЕНИЕ ATI\курс QA\модуль 15\yesterday.txt'
with open(name_f, encoding='utf-8-sig') as f:
    text = f.read()
    text = text.lower()
    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        text = text.replace(i, '')

    text = text.split()
# print('text', text) # выводит текст в виде списка(после split)

count_freg = {}  # словарь - слово :максимальная частота
freg = 1  # счетчик частоты слова в тексте
len_word = 1  # счетчик длинны слова
engl_word = {}  # словарь - английское слово:его длинна
for word in text:
    if text.count(word) > freg and len(word) > 3:  # сравниваем часто слов в тексте
        freg = text.count(word)  # присваиваем счетчику частоту более часто встречающегося слова
        count_freg = {word: freg}  # словарь - слово:частота
    elif text.count(word) == freg and len(word) > 3:  # ищем слова с такой же частотой и длинной больше 3
        count_freg[word] = text.count(word)  # добавляем новое слово такой же частоты в словарь
    if word[0] in alphabet:  # проверка первой буквы слова
        if len(word) > len_word:  # сравниваем длинну слов
            len_word = len(word)  # присваиваем счетчику значение более длинного слова
            engl_word = {word: len(word)}  # переприсваиваем новый словарь с более длинным словом
        elif len(word) == len_word:
            engl_word[word] = len(word)  # добавляем в словарь слово такой же длинны
for j in count_freg:
    print(f'Наиболее часто встречающееся слово/слова в тексте: {j}. Частота в тексте: {count_freg[j]}')
for i in engl_word:
    print(f'Наиболее длинное английское слово/слова в тексте :{i}. Его длинна: {engl_word[i]}')