# Телефонный справочник
# _______________________________________________________

phone_book = {}
path = "phones.txt"


def open_file():
    with open(path, "r", encoding="UTF-8") as file:
        data = file.readlines()
    for i, contact in enumerate(data, 1):
        contact = contact.strip().split(";")
        phone_book[i] = contact
    # print(data)


def save_file():
    contacts = []
    for contact in phone_book.values():
        contacts.append(";".join(contact))
    with open(path, "w", encoding="UTF-8") as file:
        file.write("\n".join(contacts))


def copy_contact():
    find_contact()
    id = int(input("Введите номер контакта для создания копии: \n"))
    with open("Copy_file.txt", "a", encoding="UTF-8") as new_file:
        contacts = []
        contacts.append(phone_book[id])
        new_file.write(f"{contacts} \n")



def show_contact(pb):
    for k, v in pb.items():
        print(f"{k}. {v[0]}, {v[1]}, {v[2]}")


def add_contact():
    name = input("Введите ФИО: \n")
    phone = input("Введите телефон: \n")
    comment = input("Введите комментарий: \n")
    phone_book[max(phone_book) + 1] = [name, phone, comment]


def find_contact():
    result = {}
    key_word = input("Введите искомое слово: \n")
    for k, v in phone_book.items():
        for item in v:
            if key_word in item:
                result[k] = v
    show_contact(result)


def change_contact():
    find_contact()
    id = int(input("Введите номер контакта для изменения: \n"))
    change_name = input("Измение ФИО: \n")
    if change_name == "":
        change_name = phone_book.get(id)[0]
    change_phone = input("Измение телефон: \n")
    if change_phone == "":
        change_phone = phone_book.get(id)[1]
    change_comment = input("Измение комментарий: \n")
    if change_comment == "":
        change_comment = phone_book.get(id)[2]
    phone_book[id] = [change_name, change_phone, change_comment]
    print(*phone_book[id])


def delete_contact():
    find_contact()
    id = int(input("Введите номер контакта для удаления: \n"))
    if id == "":
        show_contact(phone_book)
    del phone_book[id]
    show_contact(phone_book)


menu = """Главное меню
1. Открыть файл
2. Сохранить файл
3. Показать контакты
4. Добавить контакты
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Копировать контакт
9. Выход"""

while True:
    print()
    print(f"{menu} \n")
    choice = int(input("Выберите пункт меню: "))
    match choice:
        case 1:
            open_file()
        case 2:
            save_file()
        case 3:
            show_contact(phone_book)
        case 4:
            add_contact()
        case 5:
            find_contact()
        case 6:
            change_contact()
        case 7:
            delete_contact()
        case 8:
            copy_contact()
        case 9:
            print("See you! xoxoxo")
            break
        case _:
            print("Неверный пункт меню, попробуйте еще раз")
