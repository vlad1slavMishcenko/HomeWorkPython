phone_book = {}
path: str = 'Telephone.txt'
def open_file():
    phone_book.clear()
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}
    print('\nТелефонная книга успешно загружена!')


def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i), contact.get('name'), contact.get('phone'), contact.get('comment')])
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    print(f'\nТелефонная книга успешно сохранена!')
    print('=' * 200 + '\n')

def show_contact(book: dict[int,dict]):
    print('\n' + '=' * 200)
    for i, cnt in book.items():
        print(f'{i}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
    print('=' * 200 + '\n')


def add_contact():
    uid = max(list(phone_book.keys()))
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    if name == '' or phone == '':
        print('Поле имени или телефона осталось пустым, контакт не добавлен')
    else:
        comment = input('Введите комментарий к контакту: ')

        phone_book[uid + 1] = {'name': name, 'phone': phone, 'comment': comment}
        print(f'\nКонтакт {name} успешно добавлен в книгу!')
        print('=' * 200 + '\n')


def search():
    result = {}
    word = input('Введите слово по которому будет осуществляться поиск: ')
    for i, contact in phone_book.items():
        if word.lower() in ' '.join(list(contact.values())).lower():
            result[i] = contact
    return result

def remove():
    result = search()
    if result != {}:
        show_contact(result)
        index = int(input('Введите ID контакта, который хотим удалить: '))
        if index in phone_book.keys():
            del_cnt = phone_book.pop(index)
            print(f'\nКонтакт {del_cnt.get("name")} успешно удален!')
            print('=' * 200 + '\n')
        else:
            print('Введен неверный ID')

            
def update_contact():
    res = search()
    show_contact(res)
    index = int(input('Введите ID контакта, который хотим изменить: '))
    name = input(' Введите новое имя контакта: ')
    phone = input('Введите телефон контакта: ')
    if name == '' or phone == '':
        print('Поле имени или телефона осталось пустым, контакт не изменен')
    else:
        comment = input('Введите комментарий к контакту: ')
        phone_book[index] = {'name': name, 'phone': phone, 'comment': comment}

def menu()-> int:
    main_menu = '''Главное меню: 
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8 Выход'''
    print(main_menu)
    while True:
        select = input('Выберете пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        print('Ошибка ввода, введите ЧИСЛО от 1 до 8')

open_file()
while True:

    select = menu()
    match select:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contact(phone_book)
        case 4:
            add_contact()
            save_file()
        case 5:
            result = search()
            show_contact(result)
        case 6:
            update_contact()
            save_file()
        case 7:
            remove()
            save_file()
        case 8:
            print("До свиданья! До новых встреч")
            break
