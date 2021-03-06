import json


def read_files(name='newsafr.json'):
    if name == 'newsafr.json':
        with open(name, encoding='utf-8') as datafile:
            json_data = json.load(datafile) 
            description_text = ''
            for items in json_data['rss']['channel']['items']:
                description_text += ' ' + items['description']
        return description_text
    elif name == 'newsafr.xml':
        import xml.etree.ElementTree as ET
        tree = ET.parse("newsafr.xml")
        root = tree.getroot() 
        xml_items = root.findall("./channel/item/description")
        description_text = ''
        for items in xml_items:
            description_text = description_text + items.text
        return description_text


def count_word(description_text):
    list_split = description_text.lower().split(' ')
    dict_word_value = {}
    for word in list_split:
        if len(word) > 6:
            if word in dict_word_value:
                dict_word_value[word] += 1
            else:
                dict_word_value[word] = 1
    return dict_word_value


def sort_top(dict_word_value):
    lambda_key = lambda dict_word_value: (dict_word_value[1], dict_word_value[1])
    sort_list = sorted(dict_word_value.items(), key=lambda_key, reverse=True)
    count = 1
    dict_top_10 = {}
    for word in sort_list:
        dict_top_10[count] = word
        count += 1
        if count == 10:
            break
    for top_10 in dict_top_10.values():
        print('  ', top_10[1], ': ', top_10[0])

    return dict_top_10


def main_menu():
    while True:
        name = input('\nВведите имя файла ( newsafr.json или  newsafr.xml ). Чтобы выйти, введите - q: ')
        if name == 'newsafr.json' or name == 'newsafr.xml':
            print('\nТоп 10 самых часто встречающихся в новостях слов длиннее 6 символов:')
            sort_top(count_word(read_files(name)))
        elif name == 'q':
            break
        else:
            print('Некорректный ввод, повторите.')


main_menu()
