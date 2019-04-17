def adv_print(*text, start='', max_line=40, in_file=0):
    start += '\n'
    x = 0
    text_out = ''
    text_out += start
    while x < len(text):
        character_count_per_line = 0
        text1 = ''
        for word in text[x].split():
            character_count_per_line += len(word)
            if character_count_per_line >= max_line:
                text1 += '\n'
                character_count_per_line = len(word)
            elif text1 != '':
                text1 += ' '
                character_count_per_line += 1
            text1 += word
        text1 += '\n'
        text_out += text1
        x += 1
    print(text_out)
    if in_file == 1:
        with open('out_file.txt', 'w', encoding='utf8') as output:
            output.write(text_out)


a = 'Информация о проверке: эта проверка обнаруживает имена, которые должны разрешаться, но не разрешаются. ' \
    'Благодаря динамической отправке и набору утки это возможно в ограниченном, но полезном количестве случаев. ' \
    'Элементы верхнего уровня и класса поддерживаются лучше, чем элементы экземпляра'

b = 'Госдума на пленарном заседании во вторник приняла в третьем, заключительном чтении законопроект об обеспечении ' \
    'устойчивой работы российского сегмента интернета в случае отключения от глобальной инфраструктуры Всемирной сети.'

c = 'Аргументы директора Центрального разведывательного управления (ЦРУ) Джины Хаспел убедили президента США Дональда' \
    ' Трампа одобрить высылку 60 российских дипломатов в связи с «делом Скрипаля». Об этом сообщает The New York ' \
    'Times со ссылкой на источники в спецслужбах США.'

adv_print(a, b, c, start='Верхушка текста', max_line=50, in_file=1)
