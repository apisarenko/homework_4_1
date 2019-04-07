def adv_print(text, start='', max_line=40, in_file=0):
    start += '\n'
    text1 = ''
    text1 = start + text1
    character_count_per_line = 0
    for word in text.split():
        character_count_per_line += len(word)
        if character_count_per_line >= max_line:
            text1 += '\n'
            character_count_per_line = len(word)
        elif text1 != '':
            text1 += ' '
            character_count_per_line += 1
        text1 += word
        if in_file == 1:
            with open('out_file.txt', 'w', encoding='utf8') as output:
                output.write(text1)
    return print(text1)


a = 'Информация о проверке: эта проверка обнаруживает имена, которые должны разрешаться, но не разрешаются. Благодаря динамической отправке и набору утки это возможно в ограниченном, но полезном количестве случаев. Элементы верхнего уровня и класса поддерживаются лучше, чем элементы экземпляра'

adv_print(a, 'Верхушка текста', 50, 1)
