import os

clear = lambda : os.system('clear')


def get_contacts():

    if 'contacts' in globals():
        return globals()['contacts']
    else:
        return []

def set_contacts(contacts):    
    globals()['contacts'] = contacts

def contact_from_string(string, separator=';'):
    info = string.split(separator)
    contact = {
        'Name' : info[0], 
        'Tel' : info[1],
        'Comment' : info[2]
        }

    return contact

def contact_to_string(contact, separator=' '):
    return f'{contact["Name"]}{separator}{contact["Tel"]}{separator}{contact["Comment"]}'


def open_file():

    file = open('phonebook.txt', 'r')
    contacts = []

    for line in file:        
        contacts.append(contact_from_string(line))
    print(f'Прочитано {len(contacts)} контакт(ов)')
    
    set_contacts(contacts)

def save_file():    
    contacts = get_contacts()
    if len(contacts) == 0:
        answer = input('У вас открыто 0 контактов. Вы уверены? \n Введите y - да n - нет: ')
        if answer.lower() != 'y':
            return
    with open('phonebook.txt', 'w') as file:        
        for line in contacts:
            file.write(contact_to_string(line, ';'))            
    print(f'Контакт(ы) {len(contacts)} сохранен(ы)')
    

def print_file():
    contacts = get_contacts()
    i = 1
    for line in contacts:
        print(f'{i}. {contact_to_string(line)}')
        i += 1
    if len(contacts) == 0:
        print('Файл контактов пуст или не открыт')

def create_contact():
    result = input('Введите Имя Телефон Комментарий (через пробел): ')
    contact = contact_from_string(result, ' ')
    contacts = get_contacts()
    contacts.append(contact)
    print('Добавлен новый контакт')
    
def edit_contact():
    print_file()
    result = int(input('Укажите какой контакт надо изменить: '))
    contacts = get_contacts()
    clear()
    contact_to_edit = contacts[result-1]
    print(contact_to_string(contact_to_edit))
    edit_contact_text = input('Введите новые Имя Телефон Комментарий (через пробел): ')
    new_contact = contact_from_string(edit_contact_text, ' ')
    contacts[result-1] = new_contact

    print('Контакт изменен')
    
    
def find_contact():
    text = input('Введите Имя или номер телефона или комментарий: ')
    contacts = list(filter(lambda contact: filter_contact(contact, text), get_contacts()))
    print(f'Найдено {len(contacts)} контакт (ов)')
    for contact in contacts:
        print(contact_to_string(contact))
    

def filter_contact(contact, text):
    return text.lower() in contact_to_string(contact).lower()

    


def del_contact():
    print_file()
    contacts = get_contacts()
    if len(contacts) == 0:
        return
    else:
        result = int(input('Укажите какой контакт надо удалить: '))
        clear()
        if result > len(contacts):
            print('Указан некорректный контакт')
            return
        contact_to_del = contacts[result-1]
        print(contact_to_string(contact_to_del))
        answer = input('Удалить контакт? \n Введите y если да, n если нет: ')

        if answer.lower == 'y':
            contacts.remove(contact_to_del)
            print('Контакт удален')

