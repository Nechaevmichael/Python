def contact_to_s():
    return input('Введите информацию для поиска')

def choose_mode():
    return input('Введите режим работы(1 - добавление, 2 - поиск)')

def new_contact():
    name = input('Введите имя: ')
    phone_number = input('Введите номер: ')
    return f'{name} || {phone_number}'

def show_found(result):
    print('Результат поиска: ')
    for i in result:
        print(i)