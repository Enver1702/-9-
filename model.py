import json

phone_book = {}
path = 'phones.json'

def open_file():
    global phone_book
    try:
     with open(path, 'r' , encoding='UTF-8') as file:
        phone_book  = json.load(file)
        return True
    except:
        return False

def save_file():
    try:
        with open((path, 'w', encoding='UTF-8') as file:
            json.dump(phone_book, file, ensure_ascii=False)
           return True
    except:
           return False
def check_id():
    if phone_book:
        return max(list(map(int,phone_book)))+1
    return 1

def search(word: str) -> dict[int:dict[str,str]]:
    result = {}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result
def add_contact(new: {int:dict[str,str]}):
    contact = {check_id(): new}
    phone_book.update(contact)

def search_word() -> str:
    return input(text.search_word)

def edit_contacts(contact=None):
    print("Введите имя контакта: ")
    name = input("> ")
    for index, contact in enumerate(contact):
        if contact['name'] == name:
            print("Введите новое имя контакта: ")
            new_name = input("> ")
            print("Введите новый телефон контакта: ")
            new_phone = input("> ")
            contact_update = {
                'name': new_name,
                'phone': new_phone

def delete_contacts():
    print("Введите контакт: ")
    name = input('> ')
    for contact in delete_contacts():
        if contact['name'] == name:
            print("Удалить контакт %s (YES/NO)?: " % name)
            name_del = input('> ')
            if name_del == "YES":
                contact.remove(contact)
                print("Вы удалили контакт %s " % name)
